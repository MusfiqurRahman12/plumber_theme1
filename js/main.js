/**
 * PlumberX - Interactive JavaScript Controller
 * Site Development: Ztech Communication
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initModals();
  initTabs();
  initProjectFilter();
  initAccordion();
  initCartDrawer();
  initForms();
  initCouponPrint();
  initMarquees();
});

// Toast notification helper
function showToast(message, type = 'success') {
  let toast = document.getElementById('toastNotice');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toastNotice';
    toast.className = 'toast-notice';
    document.body.appendChild(toast);
  }
  toast.innerHTML = `
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
      <polyline points="22 4 12 14.01 9 11.01"></polyline>
    </svg>
    <span>${message}</span>
  `;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3800);
}

// Mobile Menu
function initMobileMenu() {
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const navMenu = document.querySelector('.nav-menu');
  if (menuBtn && navMenu) {
    menuBtn.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }

  // Mobile submenu accordion
  const dropdownParents = document.querySelectorAll('.nav-item.has-dropdown');
  dropdownParents.forEach(item => {
    const link = item.querySelector('.nav-link');
    if (link && window.innerWidth <= 768) {
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          item.classList.toggle('active-mobile');
        }
      });
    }
  });
}

// Modals: Appointment, Quote, Search, Lightbox
function initModals() {
  // Book Appointment
  const bookBtns = document.querySelectorAll('.btn-book-top, .btn-schedule-appointment');
  const appointmentModal = document.getElementById('appointmentModal');
  
  // Request Free Quote
  const quoteBtns = document.querySelectorAll('.btn-request-free-quote, .btn-hero-quote');
  const quoteModal = document.getElementById('quoteModal');

  // Search Modal
  const searchBtn = document.querySelector('.search-toggle-btn');
  const searchModal = document.getElementById('searchModal');

  function openModal(modal) {
    if (modal) modal.classList.add('active');
  }

  function closeModal(modal) {
    if (modal) modal.classList.remove('active');
  }

  bookBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(appointmentModal);
    });
  });

  quoteBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(quoteModal);
    });
  });

  if (searchBtn) {
    searchBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(searchModal);
    });
  }

  // Close buttons and click outside
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    const closeBtn = overlay.querySelector('.modal-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => closeModal(overlay));
    }
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        closeModal(overlay);
      }
    });
  });
}

// Vertical Tabs & Quote Type Tabs
function initTabs() {
  // Quote Tabs (Residential / Commercial)
  const quoteTabBtns = document.querySelectorAll('.quote-tab-btn');
  quoteTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      quoteTabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const serviceInput = document.getElementById('quoteServiceType');
      if (serviceInput) {
        serviceInput.value = btn.getAttribute('data-type') || 'residential';
      }
    });
  });

  // Services Vertical Tabs
  const serviceTabBtns = document.querySelectorAll('.tab-btn-vertical');
  const servicePanels = document.querySelectorAll('.tab-content-panel');
  if (serviceTabBtns.length > 0) {
    serviceTabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        serviceTabBtns.forEach(b => b.classList.remove('active'));
        servicePanels.forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        const targetId = btn.getAttribute('data-target');
        const targetPanel = document.getElementById(targetId);
        if (targetPanel) {
          targetPanel.classList.add('active');
        }
      });
    });
  }
}

// Project Filter & Shuffle Animation
function initProjectFilter() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const projectCards = document.querySelectorAll('.gallery-card');
  const galleryGrid = document.querySelector('.gallery-grid-9');

  if (!filterBtns.length || !projectCards.length) return;

  let isAnimating = false;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (btn.classList.contains('active') || isAnimating) return;

      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filterValue = btn.getAttribute('data-filter');

      shuffleGallery(filterValue);
    });
  });

  function shuffleGallery(filter) {
    isAnimating = true;

    // 1. Capture initial positions of currently visible cards
    const initialPositions = new Map();
    projectCards.forEach(card => {
      if (card.style.display !== 'none') {
        const rect = card.getBoundingClientRect();
        initialPositions.set(card, {
          left: rect.left,
          top: rect.top,
          width: rect.width,
          height: rect.height
        });
      }
    });

    // 2. Identify cards to show and cards to hide
    const cardsToHide = [];
    const cardsToShow = [];

    projectCards.forEach(card => {
      const category = card.getAttribute('data-category') || '';
      const categories = category.split(' ');
      const isMatch = (filter === 'all' || categories.includes(filter));

      if (isMatch) {
        cardsToShow.push(card);
      } else {
        cardsToHide.push(card);
      }
    });

    // 3. Fade & scale out non-matching cards
    cardsToHide.forEach(card => {
      card.style.transition = 'opacity 0.24s cubic-bezier(0.4, 0, 0.2, 1), transform 0.24s cubic-bezier(0.4, 0, 0.2, 1)';
      card.style.opacity = '0';
      card.style.transform = 'scale(0.8) translateY(12px)';
      card.style.pointerEvents = 'none';
    });

    setTimeout(() => {
      // 4. Update display states in the DOM
      cardsToHide.forEach(card => {
        card.style.display = 'none';
        card.style.transform = '';
        card.style.opacity = '';
      });

      cardsToShow.forEach(card => {
        const wasHidden = !initialPositions.has(card);
        card.style.display = 'block';
        card.style.pointerEvents = 'auto';

        if (wasHidden) {
          card.style.opacity = '0';
          card.style.transform = 'scale(0.8) translateY(12px)';
        }
      });

      // 5. Compute FLIP delta for remaining cards
      const transforms = new Map();
      cardsToShow.forEach(card => {
        if (initialPositions.has(card)) {
          const oldPos = initialPositions.get(card);
          const newRect = card.getBoundingClientRect();
          const deltaX = oldPos.left - newRect.left;
          const deltaY = oldPos.top - newRect.top;

          if (Math.abs(deltaX) > 0.5 || Math.abs(deltaY) > 0.5) {
            transforms.set(card, `translate(${deltaX}px, ${deltaY}px)`);
          }
        }
      });

      // 6. Invert positions instantly without transition
      cardsToShow.forEach(card => {
        if (transforms.has(card)) {
          card.style.transition = 'none';
          card.style.transform = transforms.get(card);
        }
      });

      // Force layout reflow
      if (galleryGrid) galleryGrid.offsetHeight;

      // 7. Play the smooth shuffle transition with subtle stagger
      requestAnimationFrame(() => {
        cardsToShow.forEach((card, index) => {
          const delay = Math.min(index * 25, 100);
          card.style.transition = `transform 0.45s cubic-bezier(0.16, 1, 0.3, 1) ${delay}ms, opacity 0.35s ease ${delay}ms`;
          card.style.transform = 'translate(0, 0) scale(1)';
          card.style.opacity = '1';
        });

        // 8. Clean up inline styles after animation finishes
        setTimeout(() => {
          cardsToShow.forEach(card => {
            card.style.transition = '';
            card.style.transform = '';
            card.style.opacity = '';
            card.style.pointerEvents = '';
          });
          isAnimating = false;
        }, 550);
      });

    }, 240);
  }

  // Lightbox
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const zoomBtns = document.querySelectorAll('.project-zoom-btn');

  zoomBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const imgSrc = btn.getAttribute('data-img');
      if (lightboxModal && lightboxImg && imgSrc) {
        lightboxImg.src = imgSrc;
        lightboxModal.classList.add('active');
      }
    });
  });
}

// Accordion (FAQ on Repair Page)
function initAccordion() {
  const headers = document.querySelectorAll('.accordion-header');
  headers.forEach(header => {
    header.addEventListener('click', () => {
      const parent = header.parentElement;
      const isOpen = parent.classList.contains('active');

      // Close all
      document.querySelectorAll('.accordion-item').forEach(item => {
        item.classList.remove('active');
        const icon = item.querySelector('.accordion-icon');
        if (icon) icon.textContent = '+';
      });

      // Toggle current
      if (!isOpen) {
        parent.classList.add('active');
        const icon = header.querySelector('.accordion-icon');
        if (icon) icon.textContent = '−';
      }
    });
  });
}

// Shopping Cart Drawer and Add-to-Cart system
const cartState = [];

function initCartDrawer() {
  const cartToggleBtn = document.querySelector('.cart-toggle-btn');
  const cartDrawer = document.getElementById('cartDrawer');
  const cartOverlay = document.getElementById('cartDrawerOverlay');
  const closeCartBtn = document.getElementById('closeCartBtn');
  const addCartBtns = document.querySelectorAll('.btn-add-cart');

  function openCart() {
    if (cartDrawer && cartOverlay) {
      cartDrawer.classList.add('active');
      cartOverlay.classList.add('active');
    }
  }

  function closeCart() {
    if (cartDrawer && cartOverlay) {
      cartDrawer.classList.remove('active');
      cartOverlay.classList.remove('active');
    }
  }

  if (cartToggleBtn) cartToggleBtn.addEventListener('click', openCart);
  if (closeCartBtn) closeCartBtn.addEventListener('click', closeCart);
  if (cartOverlay) cartOverlay.addEventListener('click', closeCart);

  addCartBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const title = btn.getAttribute('data-title') || 'Plumbing Product';
      const price = parseFloat(btn.getAttribute('data-price') || '35.00');
      const img = btn.getAttribute('data-img') || 'assets/images/shop_item_1.jpg';

      const existing = cartState.find(item => item.title === title);
      if (existing) {
        existing.qty += 1;
      } else {
        cartState.push({ title, price, img, qty: 1 });
      }

      updateCartUI();
      showToast(`Added "${title}" to your cart!`);
      openCart();
    });
  });
}

function updateCartUI() {
  const itemsContainer = document.getElementById('cartItemsContainer');
  const totalEl = document.getElementById('cartTotalAmount');
  const badgeEl = document.getElementById('cartBadgeCount');

  if (!itemsContainer || !totalEl || !badgeEl) return;

  itemsContainer.innerHTML = '';
  let total = 0;
  let count = 0;

  if (cartState.length === 0) {
    itemsContainer.innerHTML = '<p style="text-align:center; color:#94a3b8; padding:30px 0;">Your cart is empty.</p>';
  } else {
    cartState.forEach((item, index) => {
      total += item.price * item.qty;
      count += item.qty;
      const row = document.createElement('div');
      row.className = 'cart-item';
      row.innerHTML = `
        <img src="${item.img}" alt="${item.title}">
        <div class="cart-item-info">
          <div class="cart-item-title">${item.title}</div>
          <div class="cart-item-price">$${item.price.toFixed(2)} × ${item.qty}</div>
        </div>
        <button onclick="removeFromCart(${index})" style="background:none; border:none; color:#ef4444; cursor:pointer; font-size:16px;">&times;</button>
      `;
      itemsContainer.appendChild(row);
    });
  }

  totalEl.textContent = `$${total.toFixed(2)}`;
  badgeEl.textContent = count;
}

window.removeFromCart = function(index) {
  cartState.splice(index, 1);
  updateCartUI();
  showToast('Item removed from cart.');
};

// Form handling
function initForms() {
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Thank you! Your request has been sent successfully. Our team will contact you shortly.');
      form.reset();
      document.querySelectorAll('.modal-overlay').forEach(modal => modal.classList.remove('active'));
    });
  });
}

// Print coupon
function initCouponPrint() {
  const printLinks = document.querySelectorAll('.coupon-print-link');
  printLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      window.print();
    });
  });
}

// Smooth Marquee Touch Controller (Pauses on touch, resumes smoothly after release)
function initMarquees() {
  const marquees = document.querySelectorAll('.testimonials-marquee, .partner-logos-marquee');
  marquees.forEach(marquee => {
    const track = marquee.querySelector('.testimonials-track, .partner-logos-track');
    if (!track) return;

    let resumeTimer = null;

    marquee.addEventListener('touchstart', () => {
      clearTimeout(resumeTimer);
      track.style.animationPlayState = 'paused';
    }, { passive: true });

    marquee.addEventListener('touchend', () => {
      clearTimeout(resumeTimer);
      resumeTimer = setTimeout(() => {
        track.style.animationPlayState = 'running';
      }, 1200);
    }, { passive: true });
  });
}

