<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>Pessoas pelo Mundo</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn v-for="pais in paises" :key="pais" :to="'/paises/' + pais" text>
      {{ pais }}
    </v-btn>
  </v-app-bar>
</template>

<script>
import axios from "axios";

export default {
  name: "NavigationBar",
  data() {
    return {
      paises: [],
    };
  },
  async created() {
    try {
      const res = await axios.get("http://127.0.0.1:5000/paises");
      this.paises = res.data;
    } catch (error) {
      console.error("Erro ao buscar os dados dos países:", error);
    }
  }
};
</script>
