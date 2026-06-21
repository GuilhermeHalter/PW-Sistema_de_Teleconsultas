import { createRouter, createWebHistory } from 'vue-router'

import CadastroView from '../view/auth/CadastroView.vue'
import LoginView from '../view/auth/LoginView.vue'
import HomeView from '../view/HomeView.vue'
import PerfilView from '../view/PerfilView.vue'
import PerfilMedicoView from '../view/PerfilMedicoView.vue'

import DashboardPacienteView from '../view/patient/DashboardPacienteView.vue'
import HistoricoConsultaView from '../view/patient/HistoricoConsultaView.vue'
import SalaTeleconsultaView from '../view/patient/SalaTeleconsultaView.vue'
import PagamentoView from '../view/patient/PagamentoView.vue'
import AgendarConsultasView from '../view/patient/AgendarConsultasView.vue'
import HorariosConsultasView from '../view/patient/HorariosConsultasView.vue'

import DashboardMedicoView from '../view/doctor/DashboardMedicoView.vue'
import ListaConsultaView from '../view/doctor/ListaConsultaView.vue'
import GerenciarHorariosView from '../view/doctor/GerenciarHorariosView.vue'
import MinhaAgendaView from '../view/doctor/MinhaAgendaView.vue'

import AdminDashboardView from '../view/admin/AdminDashboardView.vue'
import AdminMedicosView from '../view/admin/AdminMedicosView.vue'
import AdminPacientesView from '../view/admin/AdminPacientesView.vue'
import AdminEspecialidadesView from '../view/admin/AdminEspecialidadesView.vue'
import AdminConsultasView from '../view/admin/AdminConsultasView.vue'
import AdminHorariosView from '../view/admin/AdminHorariosView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/cadastro', name: 'cadastro', component: CadastroView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/', name: 'home', component: HomeView },

    // Paciente
    { path: '/perfil', name: 'perfil', component: PerfilView, meta: { requiresAuth: true, role: 'PACIENTE' } },
    { path: '/dashboard-paciente', name: 'dashboard-paciente', component: DashboardPacienteView, meta: { requiresAuth: true, role: 'PACIENTE' } },
    { path: '/historico-consultas', name: 'historico-consultas', component: HistoricoConsultaView, meta: { requiresAuth: true, role: 'PACIENTE' } },
    { path: '/sala-teleconsulta', name: 'sala-teleconsulta', component: SalaTeleconsultaView, meta: { requiresAuth: true } },
    { path: '/pagamento', name: 'pagamento', component: PagamentoView, meta: { requiresAuth: true, role: 'PACIENTE' } },
    { path: '/agendamento-consulta', name: 'agendamento', component: AgendarConsultasView, meta: { requiresAuth: true, role: 'PACIENTE' } },
    { path: '/horarios-consulta', name: 'horarios-consulta', component: HorariosConsultasView, meta: { requiresAuth: true, role: 'PACIENTE' } },

    // Médico
    { path: '/perfil-medico', name: 'perfil-medico', component: PerfilMedicoView, meta: { requiresAuth: true, role: 'MEDICO' } },
    { path: '/dashboard-medico', name: 'dashboard-medico', component: DashboardMedicoView, meta: { requiresAuth: true, role: 'MEDICO' } },
    { path: '/gerenciar-horarios', name: 'gerenciar-horarios', component: GerenciarHorariosView, meta: { requiresAuth: true, role: 'MEDICO' } },
    { path: '/minha-agenda', name: 'minha-agenda', component: MinhaAgendaView, meta: { requiresAuth: true, role: 'MEDICO' } },
    { path: '/lista-consultas', name: 'lista-consultas', component: ListaConsultaView, meta: { requiresAuth: true, role: 'MEDICO' } },
    { path: '/sala-teleconsulta-medico', name: 'sala-teleconsulta-medico', component: SalaTeleconsultaView, meta: { requiresAuth: true, role: 'MEDICO' } },

    // Admin
    { path: '/admin/dashboard', name: 'admin-dashboard', component: AdminDashboardView, meta: { requiresAuth: true, role: 'ADMIN' } },
    { path: '/admin/medicos', name: 'admin-medicos', component: AdminMedicosView, meta: { requiresAuth: true, role: 'ADMIN' } },
    { path: '/admin/pacientes', name: 'admin-pacientes', component: AdminPacientesView, meta: { requiresAuth: true, role: 'ADMIN' } },
    { path: '/admin/especialidades', name: 'admin-especialidades', component: AdminEspecialidadesView, meta: { requiresAuth: true, role: 'ADMIN' } },
    { path: '/admin/consultas', name: 'admin-consultas', component: AdminConsultasView, meta: { requiresAuth: true, role: 'ADMIN' } },
    { path: '/admin/horarios', name: 'admin-horarios', component: AdminHorariosView, meta: { requiresAuth: true, role: 'ADMIN' } },
  ],
})

router.beforeEach((to, _from, next) => {
  const token = localStorage.getItem('access_token')
  const role = localStorage.getItem('user_role')

  if (to.meta.requiresAuth && !token) {
    return next({ name: 'login' })
  }

  if (to.meta.role && to.meta.role !== role) {
    if (role === 'MEDICO') return next({ name: 'dashboard-medico' })
    if (role === 'PACIENTE') return next({ name: 'dashboard-paciente' })
    if (role === 'ADMIN') return next({ name: 'admin-dashboard' })
    return next({ name: 'login' })
  }

  next()
})

export default router
