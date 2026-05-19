import { createRouter, createWebHistory } from 'vue-router'

import CadastroView from '../view/auth/CadastroView.vue';
import LoginView from '../view/auth/LoginView.vue';
import HomeView from '../view/HomeView.vue';
import PerfilView from '../view/PerfilView.vue';
import PerfilMedicoView from '../view/PerfilMedicoView.vue'

import DashboardPacienteView from '../view/patient/DashboardPacienteView.vue';
import HistoricoConsultaView from '../view/patient/HistoricoConsultaView.vue';
import SalaTeleconsultaView from '../view/patient/SalaTeleconsultaView.vue';
import PagamentoView from '../view/patient/PagamentoView.vue';
import AgendarConsultasView from '../view/patient/AgendarConsultasView.vue';
import HorariosConsultasView from '../view/patient/HorariosConsultasView.vue';

import DashboardMedicoView from '../view/doctor/DashboardMedicoView.vue';
import ListaConsultaView from '../view/doctor/ListaConsultaView.vue';
import GerenciarHorariosView from '../view/doctor/GerenciarHorariosView.vue';
import MinhaAgendaView from '../view/doctor/MinhaAgendaView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/cadastro', name: 'cadastro', component: CadastroView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/', name: 'home', component: HomeView },
    { path: '/perfil', name: 'perfil', component: PerfilView },
    { path: '/perfil-medico', name: 'perfil-medico', component: PerfilMedicoView },
    { path: '/dashboard-paciente', name: 'dashboard-paciente', component: DashboardPacienteView },
    { path: '/historico-consultas', name: 'historico-consultas', component: HistoricoConsultaView },
    { path: '/sala-teleconsulta', name: 'sala-teleconsulta', component: SalaTeleconsultaView },
    { path: '/pagamento', name: 'pagamento', component: PagamentoView },
    { path: '/agendamento-consulta', name: 'agendamento', component: AgendarConsultasView},
    { path: '/horarios-consulta', name: 'horarios-consulta', component: HorariosConsultasView },
    { path: '/dashboard-medico', name: 'dashboard-medico', component: DashboardMedicoView },
    { path: '/gerenciar-horarios', name: 'gerenciar-horarios', component: GerenciarHorariosView },
    { path: '/minha-agenda', name: 'minha-agenda', component: MinhaAgendaView },
    { path: '/lista-consultas', name: 'lista-consultas', component: ListaConsultaView },
  ],
})

export default router
