import Swiper from 'swiper';
import { Pagination, Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

const swiper = new Swiper('.swiper-adviсe', {
	modules: [Pagination, Navigation],
  loop: true,
  pagination: {
    el: '.swiper-pagination',
		clickable: false,
  },
	navigation: {
    nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
  },
	
	//slidesPerView: 3,
	slidesPerView: "auto",
	watchOverflow: true,
	spaceBetween: 20,
});

const swiperPartners = new Swiper('.swiper-partners', {
	slidesPerView: "auto",
	watchOverflow: true,
	spaceBetween: 0,
	freeMode: true,
/* 	mousewheel:{
		sensitivity: 10,
	}, */
});


const swiperPortfolio = new Swiper('.portfolio-swiper', {
	modules: [Navigation],
	navigation: {
    nextEl: '.portfolio-swiper-button-next',
		prevEl: '.portfolio-swiper-button-prev',
  },
  loop: true,
	slidesPerView: "auto",
	watchOverflow: true,
	spaceBetween: 20,
	freeMode: true,
	direction: 'vertical',
/* 	mousewheel:{
		sensitivity: 10,
	}, */
});