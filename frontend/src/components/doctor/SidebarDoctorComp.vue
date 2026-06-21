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
      <router-link to="/dashboard-medico" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-grid-fill"></i>
        <span>Dashboard</span>
      </router-link>

      <router-link to="/minha-agenda" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-calendar-event"></i>
        <span>Minha Agenda</span>
      </router-link>

      <router-link to="/gerenciar-horarios" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-calendar2-week"></i>
        <span>Gerenciar Horários</span>
      </router-link>

      <router-link to="/lista-consultas" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-clock-history"></i>
        <span>Histórico de Consultas</span>
      </router-link>

      <router-link to="/perfil-medico" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-person"></i>
        <span>Perfil</span>
      </router-link>
    </nav>

    <div class="user-profile mt-auto p-2 rounded-3">
      <div class="d-flex align-items-center gap-2 mb-2">
        <div class="avatar bg-white text-primary-custom rounded-circle d-flex align-items-center justify-content-center shadow-sm">
          <i class="bi bi-person-fill"></i>
        </div>
        <div class="overflow-hidden">
          <p class="mb-0 fw-bold text-dark small text-truncate">
            Dr. {{ nomeMedico }}
          </p>
          <small class="text-muted d-block" style="font-size: 0.7rem;">Médico</small>
        </div>
      </div>
      
      <button class="btn btn-logout w-100 d-flex align-items-center justify-content-center gap-2" @click="handleLogout">
        <i class="bi bi-box-arrow-right"></i> 
        <span>Sair</span>
      </button>
    </div>
  </aside>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { medicoService } from '../../services/api.js'

const router = useRouter()

// Inicializa imediatamente com o cache do localStorage salvando tempo de tela piscando vazio
const nomeMedico = ref(localStorage.getItem('user_name') || 'Médico')

const handleLogout = () => {
  // Limpa os tokens e estados guardados
  localStorage.clear()
  // Redireciona de volta para a tela de login pelo nome nominal da rota
  router.push({ name: 'login' })
}

onMounted(async () => {
  try {
    // Faz a consulta assíncrona ao endpoint do médico atual
    const res = await medicoService.getMe()
    
    // Mapeia de forma inteligente protegendo a propriedade com a grafia exata do seu Django (NomeCompleto)
    const nomeBackend = res.data.NomeCompleto || res.data.nomeCompleto || res.data.nome
    
    if (nomeBackend) {
      nomeMedico.value = nomeBackend
      localStorage.setItem('user_name', nomeBackend)
    }
  } catch (error) {
    console.error('Não foi possível atualizar os dados em tempo real do médico:', error)
  }
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.sidebar { 
  width: 260px; 
  height: 100vh; 
  background-color: #DFF2F0; 
  border-right: 1px solid #c5e5e2; 
  position: sticky; 
  top: 0; 
  overflow-y: auto; 
}

.logo-icon { 
  width: 38px; 
  height: 38px; 
  font-size: 1.2rem; 
  background-color: #0060B4; 
}

.nav-link { 
  color: #475569; 
  font-weight: 500; 
  font-size: 0.95rem; 
  transition: all 0.2s ease; 
}

.nav-link i { 
  color: #03A1E0; 
  font-size: 1.2rem; 
}

.nav-link.active { 
  background-color: #0468BF !important; 
  color: #fff !important; 
}

.nav-link.active i { 
  color: #fff !important; 
}

.nav-link:hover:not(.active) { 
  background-color: #98DEF8; 
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

.btn-logout { 
  background-color: transparent; 
  border: 1px solid #cbd5e1; 
  color: #64748b; 
  font-size: 0.8rem; 
  padding: 6px 10px; 
  border-radius: 8px; 
  transition: all 0.2s; 
}

.btn-logout:hover { 
  background-color: #fee2e2; 
  border-color: #fca5a5; 
  color: #dc2626; 
}
</style>