import { createRouter, createWebHistory } from 'vue-router';

import HomePage from './pages/HomePage.vue';
import LoginPage from './pages/auth/LoginPage.vue';
import RegisterPage from './pages/auth/RegisterPage.vue';
import NewBook from './pages/books/NewBook.vue';
import BooksList from './pages/books/BooksList.vue';
import NotFound from './pages/NotFound.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: HomePage,
    },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage },
    { path: '/newBook', component: NewBook },
    { path: '/booksList', component: BooksList },
    { path: '/:notFound(.*)', component: NotFound },
  ],
});

export default router;
