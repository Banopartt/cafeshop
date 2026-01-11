let currentIndex = 0;

function slideRight() {
    const slider = document.getElementById("slider");
    currentIndex++;
    slider.style.transform = `translateX(-${currentIndex * 310}px)`;
}

function slideLeft() {
    const slider = document.getElementById("slider");
    currentIndex = Math.max(0, currentIndex - 1);
    slider.style.transform = `translateX(-${currentIndex * 310}px)`;
}
