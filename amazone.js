/* Interactive behaviours for the static storefront prototype. */
(() => {
    const slides = Array.from(
        document.querySelectorAll(".header-slider ul img")
    );
    const previousButton = document.querySelector(".control_prev");
    const nextButton = document.querySelector(".control_next");
    const productRails = Array.from(document.querySelectorAll(".products"));

    let activeSlide = 0;

    function showSlide(requestedIndex) {
        if (slides.length === 0) {
            return;
        }

        activeSlide = (requestedIndex + slides.length) % slides.length;

        slides.forEach((slide, index) => {
            const isActive = index === activeSlide;
            slide.style.display = isActive ? "block" : "none";

            if (typeof slide.setAttribute === "function") {
                slide.setAttribute("aria-hidden", String(!isActive));
            }
        });
    }

    function bindCarouselControl(control, direction) {
        if (!control || typeof control.addEventListener !== "function") {
            return;
        }

        control.addEventListener("click", (event) => {
            if (event && typeof event.preventDefault === "function") {
                event.preventDefault();
            }

            showSlide(activeSlide + direction);
        });
    }

    if (slides.length > 0) {
        showSlide(0);
    }

    bindCarouselControl(previousButton, -1);
    bindCarouselControl(nextButton, 1);

    productRails.forEach((rail) => {
        rail.addEventListener(
            "wheel",
            (event) => {
                if (!event || Math.abs(event.deltaY) <= Math.abs(event.deltaX)) {
                    return;
                }

                const maxScroll = Math.max(0, rail.scrollWidth - rail.clientWidth);
                const nextScrollLeft = Math.min(
                    maxScroll,
                    Math.max(0, rail.scrollLeft + event.deltaY)
                );

                // At either end, allow the page itself to keep scrolling.
                if (nextScrollLeft === rail.scrollLeft) {
                    return;
                }

                event.preventDefault();
                rail.scrollLeft = nextScrollLeft;
            },
            { passive: false }
        );
    });
})();
