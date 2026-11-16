/**
 * Browser interactions for the Amazon-inspired static storefront.
 *
 * This file intentionally has no framework or package dependency. It only
 * enhances elements already present in index.html:
 *   - the promotional hero carousel;
 *   - horizontally scrollable product collections.
 *
 * Search, accounts, cart, checkout, and product navigation are not implemented
 * here. Keep this boundary explicit when adding future interactions.
 */
(() => {
    const slides = Array.from(
        document.querySelectorAll(".header-slider .header-slides img")
    );
    const previousButton = document.querySelector(".control_prev");
    const nextButton = document.querySelector(".control_next");
    const productRails = Array.from(document.querySelectorAll(".products"));

    // The carousel is intentionally page-local. No storage or network request
    // is needed because the slide collection is already present in the HTML.
    let activeSlide = 0;

    /**
     * Display one slide and hide every other slide.
     *
     * Modulo arithmetic provides wrap-around in both directions. The empty
     * collection guard prevents a division-by-zero/invalid-index operation
     * when the carousel markup is removed or conditionally unavailable.
     *
     * @param {number} requestedIndex - Desired zero-based slide position.
     */
    function showSlide(requestedIndex) {
        if (slides.length === 0) {
            return;
        }

        activeSlide = (requestedIndex + slides.length) % slides.length;

        slides.forEach((slide, index) => {
            const isActive = index === activeSlide;
            slide.style.display = isActive ? "block" : "none";

            // Keep the accessibility state aligned with visual visibility.
            // This does not replace a complete screen-reader carousel review.
            if (typeof slide.setAttribute === "function") {
                slide.setAttribute("aria-hidden", String(!isActive));
            }
        });
    }

    /**
     * Attach a direction-aware click handler to an available carousel button.
     *
     * @param {Element|null} control - Previous or next button.
     * @param {-1|1} direction - Slide movement direction.
     */
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

    // Initialize only when at least one image exists. Missing controls are
    // tolerated independently so partial markup does not crash the page.
    if (slides.length > 0) {
        showSlide(0);
    }

    bindCarouselControl(previousButton, -1);
    bindCarouselControl(nextButton, 1);

    /**
     * Translate vertical-dominant wheel input into horizontal rail movement.
     *
     * Native horizontal trackpad input is left alone. The proposed position is
     * clamped to the rail's valid range. At either boundary the event is not
     * cancelled, allowing the document itself to continue scrolling.
     */
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

                // Real WheelEvent instances provide preventDefault. Keep the
                // guard so the behaviour remains safe in lightweight test
                // environments and synthetic event integrations.
                if (typeof event.preventDefault === "function") {
                    event.preventDefault();
                }

                rail.scrollLeft = nextScrollLeft;
            },
            { passive: false }
        );
    });
})();
