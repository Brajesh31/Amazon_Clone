const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const source = fs.readFileSync(
    path.join(__dirname, "..", "amazone.js"),
    "utf8"
);

function createElement({ scrollLeft = 0, scrollWidth = 300, clientWidth = 100 } = {}) {
    const listeners = new Map();
    const attributes = {};

    return {
        style: {},
        attributes,
        scrollLeft,
        scrollWidth,
        clientWidth,
        listeners,
        addEventListener(name, callback, options) {
            listeners.set(name, { callback, options });
        },
        setAttribute(name, value) {
            attributes[name] = value;
        },
        dispatch(name, event = {}) {
            const listener = listeners.get(name);
            assert.ok(listener, `Expected a listener for ${name}`);
            listener.callback(event);
        },
    };
}

function boot({ slideCount = 3, includeControls = true, railCount = 1 } = {}) {
    const slides = Array.from({ length: slideCount }, () => createElement());
    const previous = includeControls ? createElement() : null;
    const next = includeControls ? createElement() : null;
    const rails = Array.from({ length: railCount }, () => createElement({ scrollLeft: 50 }));

    const document = {
        querySelectorAll(selector) {
            if (selector === ".header-slider ul img") return slides;
            if (selector === ".products") return rails;
            return [];
        },
        querySelector(selector) {
            if (selector === ".control_prev") return previous;
            if (selector === ".control_next") return next;
            return null;
        },
    };

    vm.runInNewContext(source, { document });
    return { slides, previous, next, rails };
}

test("shows only the first hero image on startup", () => {
    const { slides } = boot();

    assert.deepEqual(
        slides.map((slide) => slide.style.display),
        ["block", "none", "none"]
    );
    assert.deepEqual(
        slides.map((slide) => slide.attributes["aria-hidden"]),
        ["false", "true", "true"]
    );
});

test("next and previous controls change the active image", () => {
    const { slides, next, previous } = boot();
    let prevented = 0;

    next.dispatch("click", { preventDefault: () => prevented++ });
    assert.deepEqual(
        slides.map((slide) => slide.style.display),
        ["none", "block", "none"]
    );

    previous.dispatch("click", { preventDefault: () => prevented++ });
    assert.deepEqual(
        slides.map((slide) => slide.style.display),
        ["block", "none", "none"]
    );
    assert.equal(prevented, 2);
});

test("carousel navigation wraps in both directions", () => {
    const { slides, next, previous } = boot();

    previous.dispatch("click", { preventDefault() {} });
    assert.deepEqual(
        slides.map((slide) => slide.style.display),
        ["none", "none", "block"]
    );

    next.dispatch("click", { preventDefault() {} });
    assert.deepEqual(
        slides.map((slide) => slide.style.display),
        ["block", "none", "none"]
    );
});

test("vertical wheel movement scrolls a product rail horizontally", () => {
    const { rails } = boot();
    let prevented = false;

    rails[0].dispatch("wheel", {
        deltaX: 0,
        deltaY: 45,
        preventDefault() {
            prevented = true;
        },
    });

    assert.equal(rails[0].scrollLeft, 95);
    assert.equal(prevented, true);
});

test("native horizontal wheel movement is not intercepted", () => {
    const { rails } = boot();
    let prevented = false;

    rails[0].dispatch("wheel", {
        deltaX: 25,
        deltaY: 0,
        preventDefault() {
            prevented = true;
        },
    });

    assert.equal(rails[0].scrollLeft, 50);
    assert.equal(prevented, false);
});

test("wheel movement at the end of a rail does not trap page scrolling", () => {
    const { rails } = boot();
    rails[0].scrollLeft = rails[0].scrollWidth - rails[0].clientWidth;
    let prevented = false;

    rails[0].dispatch("wheel", {
        deltaX: 0,
        deltaY: 40,
        preventDefault() {
            prevented = true;
        },
    });

    assert.equal(prevented, false);
});

test("script tolerates an empty carousel and missing controls", () => {
    assert.doesNotThrow(() => boot({ slideCount: 0, includeControls: false }));
});

test("each product rail receives its own wheel handler", () => {
    const { rails } = boot({ railCount: 3 });

    assert.equal(rails.length, 3);
    for (const rail of rails) {
        assert.ok(rail.listeners.has("wheel"));
    }
});
