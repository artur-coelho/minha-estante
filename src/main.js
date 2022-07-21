import { createApp } from 'vue';

import router from './router';
import App from './App.vue';

import BaseButton from '@/components/ui/BaseButton.vue';
import BaseCard from '@/components/ui/BaseCard.vue';
import FormCard from '@/components/ui/FormCard.vue';
import BaseToggle from '@/components/ui/BaseToggle.vue';

const app = createApp(App);

app.use(router);

app.component('base-button', BaseButton);
app.component('base-card', BaseCard);
app.component('form-card', FormCard);
app.component('base-toggle', BaseToggle);

app.mount('#app');
