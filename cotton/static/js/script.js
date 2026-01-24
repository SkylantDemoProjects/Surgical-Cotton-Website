document.querySelector('.enquire-btn').addEventListener('click', () => {
    alert('Thank you for enquiring! We will contact you soon.');
});



<script>
    // Simple dot slider auto-scroll effect
    let index = 0;
    const slides = document.querySelector('.product-slider');
    const dots = document.querySelectorAll('.dot');
    const total = dots.length;

    function showSlide() {
      slides.style.transform = `translateX(-${index * 100}%)`;
      dots.forEach((dot, i) => dot.classList.toggle('active', i === index));
      index = (index + 1) % total;
    }

    setInterval(showSlide, 3000);
  </script>





// Scroll animation
window.addEventListener("scroll", function() {
  const elements = document.querySelectorAll(".fade-in");
  elements.forEach(el => {
    const position = el.getBoundingClientRect().top;
    if (position < window.innerHeight - 100) {
      el.classList.add("visible");
    }
  });
});



// Simple scroll animation for hero button
document.querySelector('.btn[href="#products"]').addEventListener('click', (e) => {
    e.preventDefault();
    document.querySelector('#products').scrollIntoView({ behavior: 'smooth' });
});










