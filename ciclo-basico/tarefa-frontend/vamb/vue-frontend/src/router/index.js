import { createRouter, createWebHistory } from "vue-router";
import PaisDetalhes from "../views/PaisDetalhes.vue";

const routes = [
  { path: "/paises/:pais", component: PaisDetalhes },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
