document.addEventListener('DOMContentLoaded', () => {
    // Scroll listener for nav header and back-to-top button
    const backToTopBtn = document.getElementById('btn-back-to-top');
    const mobileMenuToggle = document.getElementById('btn-mobile-menu');
    const navLinks = document.querySelector('.nav-links');
    
    // Mobile Menu toggle functionality
    if (mobileMenuToggle && navLinks) {
        mobileMenuToggle.addEventListener('click', () => {
            mobileMenuToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // Close menu when navigation links are clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuToggle.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }
    
    // Scroll effects
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('.nav-header');
        if (nav) {
            if (window.scrollY > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        }
        
        // Toggle Back to Top button visibility
        if (backToTopBtn) {
            if (window.scrollY > 400) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        }
    });

    // Scroll to top on click
    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Intersection Observer for fade-ups
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up').forEach((el) => {
        observer.observe(el);
    });
    
    // Trigger initial fade up for hero
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        setTimeout(() => {
            heroContent.classList.add('visible');
        }, 100);
    }

    // Sub-navigation scrollspy
    const subNavLinks = document.querySelectorAll('.sub-nav-links a[href^="#"]');
    if (subNavLinks.length > 0) {
        const sections = Array.from(subNavLinks).map(link => {
            const id = link.getAttribute('href');
            if (!id || id === '#' || id.trim() === '' || !id.startsWith('#')) return null;
            try {
                return document.querySelector(id);
            } catch (err) {
                console.warn(`Invalid scrollspy selector: ${id}`, err);
                return null;
            }
        }).filter(section => section !== null);

        function updateScrollspy() {
            let activeSection = null;
            const scrollPos = window.scrollY + 160; // offset for main nav + sub-nav + buffer

            sections.forEach(section => {
                const top = section.offsetTop;
                const height = section.offsetHeight;
                if (scrollPos >= top && scrollPos < top + height) {
                    activeSection = section;
                }
            });

            if (!activeSection && sections.length > 0) {
                if (window.scrollY < sections[0].offsetTop) {
                    activeSection = sections[0];
                } else if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 50) {
                    activeSection = sections[sections.length - 1];
                }
            }

            if (activeSection) {
                const id = activeSection.getAttribute('id');
                subNavLinks.forEach(link => {
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    } else {
                        link.classList.remove('active');
                    }
                });
            }
        }

        window.addEventListener('scroll', updateScrollspy);
        window.addEventListener('resize', updateScrollspy);
        window.addEventListener('load', updateScrollspy);
        setTimeout(updateScrollspy, 300);
        updateScrollspy();
    }

    // Get Updates Modal Functionality
    const modal = document.getElementById('updates-modal');
    const modalFormState = document.getElementById('modal-form-state');
    const modalSuccessState = document.getElementById('modal-success-state');

    window.openUpdatesModal = function() {
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
            if (modalFormState) modalFormState.style.display = 'block';
            if (modalSuccessState) modalSuccessState.style.display = 'none';
            const form = document.getElementById('newsletter-modal-form');
            if (form) form.reset();
        }
    };

    window.closeUpdatesModal = function() {
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

    window.showModalSuccess = function() {
        if (modalFormState) modalFormState.style.display = 'none';
        if (modalSuccessState) modalSuccessState.style.display = 'flex';
    };

    // Attach click listeners to any "Get Updates" button/trigger
    document.querySelectorAll('.btn-nav-updates, .trigger-updates-modal').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            // Close mobile menu if active
            const mobileMenuToggle = document.getElementById('btn-mobile-menu');
            const navLinks = document.querySelector('.nav-links');
            if (mobileMenuToggle && navLinks) {
                mobileMenuToggle.classList.remove('active');
                navLinks.classList.remove('active');
            }
            window.openUpdatesModal();
        });
    });

    const btnCloseModal = document.getElementById('btn-close-modal');
    if (btnCloseModal) {
        btnCloseModal.addEventListener('click', window.closeUpdatesModal);
    }

    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                window.closeUpdatesModal();
            }
        });
    }

    // Team Bio Modal Functionality
    const teamModal = document.getElementById('team-modal');
    const teamModalName = document.getElementById('team-modal-name');
    const teamModalRole = document.getElementById('team-modal-role');
    const teamModalBio = document.getElementById('team-modal-bio');
    const teamModalPhotoContainer = document.querySelector('.team-modal-photo-container');
    const teamModalPlaceholder = document.querySelector('.team-modal-placeholder');
    const btnCloseTeamModal = document.getElementById('btn-close-team-modal');

    window.openTeamModal = function(card) {
        if (!teamModal) return;

        const name = card.getAttribute('data-name');
        const role = card.getAttribute('data-role');
        const img = card.getAttribute('data-img');
        const bio = card.getAttribute('data-bio');

        if (teamModalName) teamModalName.textContent = name;
        if (teamModalRole) teamModalRole.textContent = role;
        if (teamModalBio) teamModalBio.textContent = bio;

        if (teamModalPhotoContainer) {
            if (img) {
                teamModalPhotoContainer.style.backgroundImage = `url('${img}')`;
                if (teamModalPlaceholder) teamModalPlaceholder.style.display = 'none';
            } else {
                teamModalPhotoContainer.style.backgroundImage = 'none';
                if (teamModalPlaceholder) {
                    const initials = name ? name.split(' ').map(n => n[0]).join('') : '';
                    teamModalPlaceholder.querySelector('span').textContent = initials;
                    teamModalPlaceholder.style.display = 'flex';
                }
            }
        }

        teamModal.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    window.closeTeamModal = function() {
        if (teamModal) {
            teamModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

    // Attach click listener to team cards
    document.querySelectorAll('.team-card').forEach(card => {
        card.addEventListener('click', (e) => {
            e.preventDefault();
            window.openTeamModal(card);
        });
    });

    if (btnCloseTeamModal) {
        btnCloseTeamModal.addEventListener('click', window.closeTeamModal);
    }

    if (teamModal) {
        teamModal.addEventListener('click', (e) => {
            if (e.target === teamModal) {
                window.closeTeamModal();
            }
        });
    }

    // Lightbox Modal for Photo Gallery, Coreshack, and Maps
    const lightboxModal = document.getElementById('gallery-lightbox-modal');
    const lightboxImg = document.getElementById('gallery-lightbox-img');
    const lightboxCaption = document.getElementById('gallery-lightbox-caption');
    const btnCloseLightbox = document.getElementById('btn-close-gallery-lightbox');
    const btnLightboxPrev = document.getElementById('btn-lightbox-prev');
    const btnLightboxNext = document.getElementById('btn-lightbox-next');

    let currentCollection = [];
    let currentIndex = 0;

    function openLightbox(collection, index) {
        currentCollection = collection;
        currentIndex = index;
        
        if (currentCollection && currentCollection.length > 0) {
            const item = currentCollection[currentIndex];
            if (lightboxImg) {
                lightboxImg.src = item.src;
                lightboxImg.alt = item.alt;
            }
            if (lightboxCaption) {
                lightboxCaption.textContent = item.caption;
            }
        }

        if (lightboxModal) {
            lightboxModal.classList.add('active');
            document.body.style.overflow = 'hidden';
            
            if (lightboxImg) {
                lightboxImg.animate([
                    { opacity: 0, transform: 'scale(0.95)' },
                    { opacity: 1, transform: 'scale(1)' }
                ], {
                    duration: 300,
                    easing: 'cubic-bezier(0.25, 1, 0.5, 1)',
                    fill: 'forwards'
                });
            }
        }
    }

    function closeLightbox() {
        if (lightboxModal) {
            lightboxModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    function updateLightbox(direction = 'next') {
        if (!currentCollection || currentCollection.length === 0) return;
        const item = currentCollection[currentIndex];
        if (!lightboxImg) return;

        const slideOutX = direction === 'next' ? '-20px' : '20px';
        const slideInX = direction === 'next' ? '20px' : '-20px';

        const fadeOut = lightboxImg.animate([
            { opacity: 1, transform: 'translateX(0) scale(1)' },
            { opacity: 0, transform: `translateX(${slideOutX}) scale(0.98)` }
        ], {
            duration: 150,
            easing: 'cubic-bezier(0.25, 1, 0.5, 1)',
            fill: 'forwards'
        });

        fadeOut.onfinish = () => {
            lightboxImg.src = item.src;
            lightboxImg.alt = item.alt;
            if (lightboxCaption) {
                lightboxCaption.textContent = item.caption;
            }

            lightboxImg.animate([
                { opacity: 0, transform: `translateX(${slideInX}) scale(0.98)` },
                { opacity: 1, transform: 'translateX(0) scale(1)' }
            ], {
                duration: 250,
                easing: 'cubic-bezier(0.25, 1, 0.5, 1)',
                fill: 'forwards'
            });
        };
    }

    // Prev/Next handlers
    if (btnLightboxPrev) {
        btnLightboxPrev.addEventListener('click', (e) => {
            e.stopPropagation();
            currentIndex = (currentIndex - 1 + currentCollection.length) % currentCollection.length;
            updateLightbox('prev');
        });
    }

    if (btnLightboxNext) {
        btnLightboxNext.addEventListener('click', (e) => {
            e.stopPropagation();
            currentIndex = (currentIndex + 1) % currentCollection.length;
            updateLightbox('next');
        });
    }

    if (btnCloseLightbox) {
        btnCloseLightbox.addEventListener('click', closeLightbox);
    }

    if (lightboxModal) {
        lightboxModal.addEventListener('click', (e) => {
            if (e.target === lightboxModal || e.target.classList.contains('lightbox-content')) {
                closeLightbox();
            }
        });
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (lightboxModal && lightboxModal.classList.contains('active')) {
            if (e.key === 'ArrowLeft') {
                btnLightboxPrev.click();
            } else if (e.key === 'ArrowRight') {
                btnLightboxNext.click();
            } else if (e.key === 'Escape') {
                closeLightbox();
            }
        }
    });
    // Populate collections dynamically (visible items only on click for correct navigation)
    const photoElements = document.querySelectorAll('[data-gallery-index]');
    photoElements.forEach((el) => {
        el.addEventListener('click', () => {
            const visiblePhotos = [];
            let clickedIndexInVisible = 0;
            let visibleIdx = 0;
            photoElements.forEach((otherEl) => {
                if (otherEl.style.display !== 'none' && !otherEl.classList.contains('hidden')) {
                    const img = otherEl.querySelector('img');
                    if (img) {
                        visiblePhotos.push({
                            src: img.getAttribute('src') || '',
                            alt: img.getAttribute('alt') || '',
                            caption: img.getAttribute('alt') || ''
                        });
                        if (otherEl === el) {
                            clickedIndexInVisible = visibleIdx;
                        }
                        visibleIdx++;
                    }
                }
            });
            openLightbox(visiblePhotos, clickedIndexInVisible);
        });
    });

    const coreElements = document.querySelectorAll('[data-core-index]');
    const coreCollection = [];
    coreElements.forEach((el, idx) => {
        const img = el.querySelector('img');
        if (img) {
            coreCollection.push({
                src: img.getAttribute('src') || '',
                alt: img.getAttribute('alt') || '',
                caption: img.getAttribute('alt') || ''
            });
            el.addEventListener('click', () => {
                openLightbox(coreCollection, idx);
            });
        }
    });

    const mapElements = document.querySelectorAll('[data-map-index]');
    const mapCollection = [];
    mapElements.forEach((el, idx) => {
        const img = el.querySelector('img');
        if (img) {
            mapCollection.push({
                src: img.getAttribute('src') || '',
                alt: img.getAttribute('alt') || '',
                caption: img.getAttribute('alt') || ''
            });
            el.addEventListener('click', () => {
                openLightbox(mapCollection, idx);
            });
        }
    });


    // Video Modal
    const videoModal = document.getElementById('gallery-video-modal');
    const videoIframe = document.getElementById('gallery-video-iframe');
    const btnCloseVideo = document.getElementById('btn-close-gallery-video');

    function openVideoModal(videoSrc) {
        if (videoIframe) {
            const src = videoSrc || "https://www.youtube.com/embed/5V9uYvN2_Xg";
            videoIframe.src = src.includes('?') ? `${src}&autoplay=1` : `${src}?autoplay=1`;
        }
        if (videoModal) {
            videoModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeVideoModal() {
        if (videoModal) {
            videoModal.classList.remove('active');
            document.body.style.overflow = '';
        }
        if (videoIframe) {
            videoIframe.src = "";
        }
    }

    document.querySelectorAll('[data-video-index]').forEach(el => {
        el.addEventListener('click', () => {
            openVideoModal();
        });
    });

    document.querySelectorAll('.video-card').forEach(el => {
        el.addEventListener('click', () => {
            const videoSrc = el.getAttribute('data-video-src');
            openVideoModal(videoSrc);
        });
    });

    if (btnCloseVideo) {
        btnCloseVideo.addEventListener('click', closeVideoModal);
    }

    if (videoModal) {
        videoModal.addEventListener('click', (e) => {
            if (e.target === videoModal) {
                closeVideoModal();
            }
        });
    }

    // Scroll Carousel utility
    window.scrollCarousel = function(carouselId, direction) {
        const carousel = document.getElementById(carouselId);
        if (!carousel) return;
        
        const scrollAmount = carousel.clientWidth * 0.8;
        if (direction === 'left') {
            carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        } else {
            carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
    };

    // Update progress bar helper
    function updateProgress(carousel, progressBar) {
        if (!carousel || !progressBar) return;
        const maxScroll = carousel.scrollWidth - carousel.clientWidth;
        if (maxScroll <= 0) {
            progressBar.style.width = '0%';
            return;
        }
        const percentage = (carousel.scrollLeft / maxScroll) * 100;
        progressBar.style.width = `${Math.min(100, Math.max(0, percentage))}%`;
    }

    // Set up scroll listeners for carousels
    const vCarousel = document.getElementById('videos-carousel');
    const vProgress = document.getElementById('videos-carousel-progress');
    if (vCarousel && vProgress) {
        vCarousel.addEventListener('scroll', () => updateProgress(vCarousel, vProgress));
        updateProgress(vCarousel, vProgress);
        window.addEventListener('resize', () => updateProgress(vCarousel, vProgress));
    }

    const pCarousel = document.getElementById('photos-carousel');
    const pProgress = document.getElementById('photos-carousel-progress');
    if (pCarousel && pProgress) {
        pCarousel.addEventListener('scroll', () => updateProgress(pCarousel, pProgress));
        updateProgress(pCarousel, pProgress);
        window.addEventListener('resize', () => updateProgress(pCarousel, pProgress));
    }

    // Segmented Control / Tab Switcher for Gallery
    const tabButtons = document.querySelectorAll('.segmented-control .tab-btn');
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.parentElement.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const targetId = btn.getAttribute('data-target');
            if (targetId) {
                const targetWrapper = document.getElementById(targetId);
                if (targetWrapper) {
                    document.querySelectorAll('.gallery-tab-content').forEach(content => {
                        content.style.display = 'none';
                    });
                    targetWrapper.style.display = 'block';
                    
                    const childCarousel = targetWrapper.querySelector('.gallery-carousel');
                    const childProgress = targetWrapper.querySelector('.carousel-progress-bar');
                    if (childCarousel && childProgress) {
                        setTimeout(() => {
                            updateProgress(childCarousel, childProgress);
                        }, 50);
                    }
                }
            }
        });
    });

    // Interactive Donut Chart for Investors page
    (function initDonutChart() {
        const segments = document.querySelectorAll('.donut-segment');
        const centerTitle = document.getElementById('donut-center-title');
        const centerValue = document.getElementById('donut-center-value');
        const legendRows = document.querySelectorAll('.legend-row');

        if (!segments.length || !centerTitle || !centerValue) return;

        const segmentData = {
            common: { title: "Common Shares", value: "210.2M" },
            warrants: { title: "Warrants", value: "90.3M" },
            options: { title: "Options", value: "18.3M" },
            default: { title: "Fully Diluted", value: "318.9M" }
        };

        function updateCenter(type) {
            const data = segmentData[type] || segmentData.default;
            centerTitle.textContent = data.title;
            centerValue.textContent = data.value;

            // Highlight corresponding legend row
            legendRows.forEach(row => {
                const rowType = row.getAttribute('data-segment');
                if (rowType === type) {
                    row.classList.add('active');
                } else {
                    row.classList.remove('active');
                }
            });
        }

        segments.forEach(segment => {
            const type = segment.getAttribute('data-segment');
            segment.addEventListener('mouseenter', () => updateCenter(type));
            segment.addEventListener('mouseleave', () => updateCenter('default'));
        });

        legendRows.forEach(row => {
            const type = row.getAttribute('data-segment');
            row.addEventListener('mouseenter', () => {
                updateCenter(type);
                // Highlight the SVG segment
                segments.forEach(seg => {
                    const segType = seg.getAttribute('data-segment');
                    if (segType === type) {
                        seg.style.strokeWidth = '30px';
                        seg.style.filter = 'drop-shadow(0 0 12px var(--copper-glow))';
                    } else {
                        seg.style.opacity = '0.4';
                    }
                });
            });
            row.addEventListener('mouseleave', () => {
                updateCenter('default');
                segments.forEach(seg => {
                    seg.style.strokeWidth = '';
                    seg.style.filter = '';
                    seg.style.opacity = '';
                });
            });
        });
    })();

    // Corporate Calendar Event Filtering & Pagination
    (function initEventsPagination() {
        const filterButtons = document.querySelectorAll('.filter-btn');
        const eventCards = document.querySelectorAll('.event-card');
        const paginationContainer = document.getElementById('events-pagination');

        if (!eventCards.length) return;

        const pageSize = 3;
        let currentFilter = 'all';
        let currentPage = 1;

        function updateEvents() {
            // Get all cards matching the filter
            const matchingCards = Array.from(eventCards).filter(card => {
                const eventType = card.getAttribute('data-event-type');
                return currentFilter === 'all' || eventType === currentFilter;
            });

            const totalEvents = matchingCards.length;
            const totalPages = Math.ceil(totalEvents / pageSize);

            // Bound current page
            if (currentPage > totalPages) currentPage = Math.max(1, totalPages);

            const startIndex = (currentPage - 1) * pageSize;
            const endIndex = startIndex + pageSize;

            // Hide all cards first
            eventCards.forEach(card => {
                card.style.display = 'none';
            });

            // Show only cards for the current page
            matchingCards.forEach((card, index) => {
                if (index >= startIndex && index < endIndex) {
                    card.style.display = 'flex';
                    // Fade-in animation
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(10px)';
                    requestAnimationFrame(() => {
                        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    });
                }
            });

            // Render pagination controls
            if (!paginationContainer) return;
            paginationContainer.innerHTML = '';

            if (totalPages <= 1) {
                return; // No need for pagination if only 1 page
            }

            // Prev Button
            const prevBtn = document.createElement('button');
            prevBtn.className = 'page-btn page-arrow';
            prevBtn.disabled = currentPage === 1;
            prevBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-left"><path d="m15 18-6-6 6-6"/></svg>
            `;
            prevBtn.addEventListener('click', () => {
                if (currentPage > 1) {
                    currentPage--;
                    updateEvents();
                    document.getElementById('events').scrollIntoView({ behavior: 'smooth' });
                }
            });
            paginationContainer.appendChild(prevBtn);

            // Numeric Buttons
            for (let i = 1; i <= totalPages; i++) {
                const numBtn = document.createElement('button');
                numBtn.className = `page-btn ${currentPage === i ? 'active' : ''}`;
                numBtn.textContent = i;
                numBtn.addEventListener('click', () => {
                    if (currentPage !== i) {
                        currentPage = i;
                        updateEvents();
                        document.getElementById('events').scrollIntoView({ behavior: 'smooth' });
                    }
                });
                paginationContainer.appendChild(numBtn);
            }

            // Next Button
            const nextBtn = document.createElement('button');
            nextBtn.className = 'page-btn page-arrow';
            nextBtn.disabled = currentPage === totalPages;
            nextBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-right"><path d="m9 18 6-6-6-6"/></svg>
            `;
            nextBtn.addEventListener('click', () => {
                if (currentPage < totalPages) {
                    currentPage++;
                    updateEvents();
                    document.getElementById('events').scrollIntoView({ behavior: 'smooth' });
                }
            });
            paginationContainer.appendChild(nextBtn);
        }

        // Filter button click event
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentFilter = btn.getAttribute('data-filter');
                currentPage = 1; // Reset to page 1 on filter change
                updateEvents();
            });
        });

        // Initial render
        updateEvents();
    })();

    // Content Gallery Photo & Video Filtering with Load More
    // --- Photos Gallery ---
    const photosGrid = document.getElementById('photos-grid');
    const photoCards = document.querySelectorAll('.photo-card');
    const photoFilters = document.querySelectorAll('#gallery-photos-wrapper .filter-pill');
    const btnPhotoLoadMore = document.getElementById('btn-load-more');
    const photoLoadMoreContainer = document.getElementById('load-more-container');

    let currentPhotoFilter = 'all';
    let visiblePhotosCount = 12;
    const photosPerPage = 12;

    function updatePhotosGallery() {
        if (!photosGrid) return;
        
        let matchingPhotos = [];
        photoCards.forEach(card => {
            const category = card.getAttribute('data-category');
            if (currentPhotoFilter === 'all' || category === currentPhotoFilter) {
                matchingPhotos.push(card);
            } else {
                card.classList.add('hidden');
                card.classList.remove('fade-in');
            }
        });

        // Show matching photos up to visiblePhotosCount
        matchingPhotos.forEach((card, idx) => {
            if (idx < visiblePhotosCount) {
                card.classList.remove('hidden');
                card.classList.add('fade-in');
            } else {
                card.classList.add('hidden');
                card.classList.remove('fade-in');
            }
        });

        // Show/hide Load More button
        if (matchingPhotos.length > visiblePhotosCount) {
            if (photoLoadMoreContainer) photoLoadMoreContainer.style.display = 'flex';
        } else {
            if (photoLoadMoreContainer) photoLoadMoreContainer.style.display = 'none';
        }
    }

    // Event listeners for photo filters
    photoFilters.forEach(pill => {
        pill.addEventListener('click', () => {
            photoFilters.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            currentPhotoFilter = pill.getAttribute('data-filter');
            visiblePhotosCount = photosPerPage; // reset
            updatePhotosGallery();
        });
    });

    // Load More Photos handler
    window.loadMorePhotos = function() {
        visiblePhotosCount += photosPerPage;
        updatePhotosGallery();
    };

    // --- Videos Gallery ---
    const videosGrid = document.getElementById('videos-grid');
    const videoCards = document.querySelectorAll('.video-card');
    const videoFilters = document.querySelectorAll('#gallery-videos-wrapper .filter-pill');
    const btnVideoLoadMore = document.getElementById('btn-video-load-more');
    const videoLoadMoreContainer = document.getElementById('video-load-more-container');

    let currentVideoFilter = 'all';
    let visibleVideosCount = 6;
    const videosPerPage = 6;

    function updateVideosGallery() {
        if (!videosGrid) return;

        let matchingVideos = [];
        videoCards.forEach(card => {
            const category = card.getAttribute('data-category');
            if (currentVideoFilter === 'all' || category === currentVideoFilter) {
                matchingVideos.push(card);
            } else {
                card.classList.add('hidden');
                card.classList.remove('fade-in');
            }
        });

        // Show matching videos up to visibleVideosCount
        matchingVideos.forEach((card, idx) => {
            if (idx < visibleVideosCount) {
                card.classList.remove('hidden');
                card.classList.add('fade-in');
            } else {
                card.classList.add('hidden');
                card.classList.remove('fade-in');
            }
        });

        // Show/hide Load More button
        if (matchingVideos.length > visibleVideosCount) {
            if (videoLoadMoreContainer) videoLoadMoreContainer.style.display = 'flex';
        } else {
            if (videoLoadMoreContainer) videoLoadMoreContainer.style.display = 'none';
        }
    }

    // Event listeners for video filters
    videoFilters.forEach(pill => {
        pill.addEventListener('click', () => {
            videoFilters.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            currentVideoFilter = pill.getAttribute('data-filter');
            visibleVideosCount = videosPerPage; // reset
            updateVideosGallery();
        });
    });

    // Load More Videos handler
    window.loadMoreVideos = function() {
        visibleVideosCount += videosPerPage;
        updateVideosGallery();
    };

    // Press Releases Filter & Search
    const pressFilters = document.querySelectorAll('.press-filters .filter-pill');
    const pressSearch = document.getElementById('press-search');
    const pressItems = document.querySelectorAll('.press-item');

    if (pressItems.length > 0 && (pressFilters.length > 0 || pressSearch)) {
        let activeCategory = 'all';
        let searchQuery = '';

        function filterPressReleases() {
            pressItems.forEach(item => {
                const category = item.getAttribute('data-category');
                const titleElement = item.querySelector('h3');
                const descElement = item.querySelector('p');
                const titleText = titleElement ? titleElement.textContent.toLowerCase() : '';
                const descText = descElement ? descElement.textContent.toLowerCase() : '';
                
                const matchesCategory = (activeCategory === 'all' || category === activeCategory);
                const matchesSearch = (titleText.includes(searchQuery) || (descText && descText.includes(searchQuery)));

                if (matchesCategory && matchesSearch) {
                    item.style.display = 'flex';
                    // Trigger a smooth fade-in animation
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(10px)';
                    item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                    requestAnimationFrame(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0)';
                    });
                } else {
                    item.style.display = 'none';
                }
            });
        }

        pressFilters.forEach(btn => {
            btn.addEventListener('click', () => {
                pressFilters.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                activeCategory = btn.getAttribute('data-filter');
                filterPressReleases();
            });
        });

        if (pressSearch) {
            pressSearch.addEventListener('input', (e) => {
                searchQuery = e.target.value.toLowerCase().trim();
                filterPressReleases();
            });
        }
    }

    // Initialize both galleries
    updatePhotosGallery();
    updateVideosGallery();
});


