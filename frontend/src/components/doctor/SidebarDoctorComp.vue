<template>
  <aside class="sidebar d-flex flex-column p-3">
    <div class="brand d-flex align-items-center gap-2 mb-5 px-2">
      <div class="logo-icon text-white rounded-circle d-flex align-items-center justify-content-center">
        <i class="bi bi-stethoscope"></i>
      </div>
      <div class="brand-text">
        <h6 class="mb-0 fw-bold text-dark">MedConnect</h6>
        <small class="text-muted" style="font-size: 0.75rem;">Portal Médico</small>
      </div>
    </div>

    <nav class="nav flex-column gap-2 flex-grow-1">
      <router-link to="/dashboard-medico" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3"
        active-class="active">
        <i class="bi bi-grid-fill"></i>
        <span>Dashboard</span>
      </router-link>

      <router-link to="/minha-agenda" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3"
        active-class="active">
        <i class="bi bi-calendar-event"></i>
        <span>Minha Agenda</span>
      </router-link>

      <router-link to="/gerenciar-horarios" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3"
        active-class="active">
        <i class="bi bi-calendar2-week"></i>
        <span>Gerenciar Horários</span>
      </router-link>

      <router-link to="/lista-consultas" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3"
        active-class="active">
        <i class="bi bi-clock-history"></i>
        <span>Histórico de Consultas</span>
      </router-link>

      <router-link to="/perfil-medico" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3"
        active-class="active">
        <i class="bi bi-person"></i>
        <span>Perfil</span>
      </router-link>
    </nav>

    <div class="user-profile mt-auto p-2 d-flex align-items-center gap-2 rounded-3">
      <div
        class="avatar bg-white text-primary-custom rounded-circle d-flex align-items-center justify-content-center shadow-sm">
        <i class="bi bi-person-fill"></i>
      </div>
      <div class="overflow-hidden">
        <p class="mb-0 fw-bold text-dark small text-truncate">
          Dr. {{ usuarioLogado.nomeCompleto }}
        </p>
        <small class="text-muted d-block" style="font-size: 0.7rem;">Médico</small>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const usuarioLogado = ref({
  nomeCompleto: 'Carregando...',
  email: ''
})

const buscarEu = async () => {
  try {
    const token = localStorage.getItem('access_token')

    const response = await axios.get('http://localhost:8000/api/medicos/me/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    usuarioLogado.value = response.data
  } catch (error) {
    console.error('Erro ao identificar utilizador:', error)
    usuarioLogado.value.nomeCompleto = 'Convidado'
  }
}

onMounted(() => {
  buscarEu()
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

/* Variáveis de escopo unificadas com a paleta padrão */
:host {
  --primary-blue: #0468BF;
  --dark-blue: #0060B4;
  --light-blue: #98DEF8;
  --sky-blue: #03A1E0;
  --bg-soft: #DFF2F0;
}

.sidebar {
  width: 260px;
  height: 100vh;
  background-color: #DFF2F0; /* Cor de fundo igual à do paciente */
  border-right: 1px solid #c5e5e2;
  position: sticky;
  top: 0;
}

.logo-icon {
  width: 38px;
  height: 38px;
  font-size: 1.2rem;
  background-color: #0060B4; /* Azul Escuro */
}

.nav-link {
  color: #475569;
  font-weight: 500;
  font-size: 0.95rem;
  transition: all 0.2s ease;
}

.nav-link i {
  color: #03A1E0; /* Ícones em azul céu */
  font-size: 1.2rem;
}

.nav-link.active {
  background-color: #0468BF !important; /* Azul de Destaque */
  color: #ffffff !important;
}

.nav-link.active i {
  color: #ffffff !important;
}

.nav-link:hover:not(.active) {
  background-color: #98DEF8; /* Hover Azul Claro */
  color: #0060B4;
}

.user-profile {
  background-color: rgba(255, 255, 255, 0.5);
  border: 1px solid #98DEF8;
}

.avatar {
  width: 36px;
  height: 36px;
  min-width: 36px;
}

.text-primary-custom {
  color: #0468BF;
}
</style>