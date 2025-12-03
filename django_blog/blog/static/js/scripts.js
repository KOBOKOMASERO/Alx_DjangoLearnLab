// ===========================
// Modern Blog Script
// ===========================
document.addEventListener('DOMContentLoaded', () => {
    
    // ----- 1. Scroll to Top Button -----
    const scrollButton = document.createElement('button');
    scrollButton.id = 'scrollTopBtn';
    scrollButton.innerText = '↑';
    scrollButton.title = 'Back to top';
    document.body.appendChild(scrollButton);

    scrollButton.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        display: none;
        transition: transform 0.3s, background-color 0.3s;
        z-index: 1000;
    `;

    scrollButton.addEventListener('mouseover', () => {
        scrollButton.style.backgroundColor = '#0056b3';
        scrollButton.style.transform = 'scale(1.1)';
    });
    scrollButton.addEventListener('mouseout', () => {
        scrollButton.style.backgroundColor = '#007bff';
        scrollButton.style.transform = 'scale(1)';
    });

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollButton.style.display = 'block';
        } else {
            scrollButton.style.display = 'none';
        }
    });

    scrollButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // ----- 2. Mobile Navigation Toggle -----
    const nav = document.querySelector('header nav ul');
    if (nav) {
        const menuToggle = document.createElement('button');
        menuToggle.id = 'menuToggle';
        menuToggle.innerHTML = '&#9776;';
        menuToggle.title = 'Menu';
        menuToggle.style.cssText = `
            display: none;
            position: absolute;
            top: 10px;
            right: 20px;
            font-size: 28px;
            background: none;
            border: none;
            color: white;
            cursor: pointer;
        `;
        nav.parentElement.appendChild(menuToggle);

        menuToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
        });

        const resizeHandler = () => {
            if (window.innerWidth <= 768) {
                menuToggle.style.display = 'block';
                nav.style.display = nav.classList.contains('active') ? 'flex' : 'none';
                nav.style.flexDirection = 'column';
                nav.style.gap = '15px';
            } else {
                menuToggle.style.display = 'none';
                nav.style.display = 'flex';
                nav.style.flexDirection = 'row';
                nav.style.gap = '25px';
            }
        };
        window.addEventListener('resize', resizeHandler);
        resizeHandler();
    }

    // ----- 3. Fade-in animation for posts -----
    const posts = document.querySelectorAll('.content ul li, article');
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                entry.target.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    posts.forEach(post => {
        post.style.opacity = '0';
        post.style.transform = 'translateY(20px)';
        observer.observe(post);
    });

});
