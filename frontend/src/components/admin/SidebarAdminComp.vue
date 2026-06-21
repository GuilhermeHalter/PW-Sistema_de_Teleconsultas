<template>
  <aside class="sidebar d-flex flex-column p-3">
    <div class="brand d-flex align-items-center gap-2 mb-5 px-2">
      <div class="logo-icon text-white rounded-circle d-flex align-items-center justify-content-center">
        <i class="bi bi-shield-fill-check"></i>
      </div>
      <div class="brand-text">
        <h6 class="mb-0 fw-bold text-dark">MedConnect</h6>
        <small class="text-muted" style="font-size: 0.75rem;">Painel Admin</small>
      </div>
    </div>

    <nav class="nav flex-column gap-2 flex-grow-1">
      <router-link to="/admin/dashboard" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-grid-fill"></i><span>Dashboard</span>
      </router-link>
      <router-link to="/admin/medicos" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-heart-pulse"></i><span>Médicos</span>
      </router-link>
      <router-link to="/admin/pacientes" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-people"></i><span>Pacientes</span>
      </router-link>
      <router-link to="/admin/consultas" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-calendar-check"></i><span>Consultas</span>
      </router-link>
      <router-link to="/admin/horarios" class="nav-link d-flex align-items-center gap-3 px-3 py-2 rounded-3" active-class="active">
        <i class="bi bi-clock"></i><span>Horários</span>
      </router-link>
    </nav>

    <div class="user-profile mt-auto p-2 rounded-3">
      <div class="d-flex align-items-center gap-2 mb-2">
        <div class="avatar bg-white text-danger rounded-circle d-flex align-items-center justify-content-center shadow-sm">
          <i class="bi bi-shield-fill"></i>
        </div>
        <div class="overflow-hidden">
          <p class="mb-0 fw-bold text-dark small text-truncate">Administrador</p>
          <small class="text-danger d-block" style="font-size: 0.7rem;">Admin</small>
        </div>
      </div>
      <button class="btn btn-logout w-100 d-flex align-items-center justify-content-center gap-2" @click="logout">
        <i class="bi bi-box-arrow-right"></i> Sair
      </button>
    </div>
  </aside>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const logout = () => {
  localStorage.clear()
  router.push({ name: 'login' })
}
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.sidebar { width: 260px; height: 100vh; background-color: #fdf2f2; border-right: 1px solid #fecaca; position: sticky; top: 0; overflow-y: auto; }
.logo-icon { width: 38px; height: 38px; font-size: 1.2rem; background-color: #dc2626; }
.nav-link { color: #475569; font-weight: 500; font-size: 0.95rem; transition: all 0.2s ease; }
.nav-link i { color: #ef4444; font-size: 1.2rem; }
.nav-link.active { background-color: #dc2626 !important; color: #fff !important; }
.nav-link.active i { color: #fff !important; }
.nav-link:hover:not(.active) { background-color: #fee2e2; color: #dc2626; }
.user-profile { background-color: rgba(255,255,255,0.5); border: 1px solid #fecaca; }
.avatar { width: 36px; height: 36px; min-width: 36px; }
.btn-logout { background-color: transparent; border: 1px solid #fca5a5; color: #64748b; font-size: 0.8rem; padding: 6px 10px; border-radius: 8px; transition: all 0.2s; }
.btn-logout:hover { background-color: #fee2e2; border-color: #fca5a5; color: #dc2626; }
</style>
