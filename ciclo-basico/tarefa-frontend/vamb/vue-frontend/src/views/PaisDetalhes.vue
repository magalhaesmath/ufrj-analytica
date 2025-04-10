<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6" v-for="pessoa in pessoas" :key="pessoa.nome">
        <v-card>
          <v-card-title>{{ pessoa.nome }} {{ pessoa.sobrenome }}</v-card-title>
          <v-card-subtitle>
            <p><strong>Idade:</strong> {{ pessoa.idade }} anos</p>
            <p><strong>Gênero:</strong> {{ pessoa.genero }}</p>
            <p><strong>Salário:</strong> {{ pessoa.salario }}</p>
            <p><strong>Cidade:</strong> {{ pessoa.cidade }}</p>
            <p><strong>País:</strong> {{ pessoa.pais }}</p>
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "PaisDetalhes",
  data() {
    return {
      pessoas: [],
    };
  },
  async created() {
    this.fetchData();
  },
  watch: {
    '$route.params.pais': 'fetchData',
  },
  methods: {
    async fetchData() {
      try {
        const pais = this.$route.params.pais;
        console.log("Buscando dados para o país:", pais);
        const res = await axios.get(`http://127.0.0.1:5000/paises/${pais}`);
        this.pessoas = res.data;
        console.log("Dados recebidos:", this.pessoas);
      } catch (error) {
        console.error("Erro ao buscar os dados das pessoas:", error);
      }
    }
  }
};
</script>
