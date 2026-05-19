<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold mb-1 text-dark">Meu Perfil</h3>
        <p class="text-muted">Gerencie suas informações profissionais e preferências</p>
      </header>

      <div class="d-flex flex-column gap-4 profile-container">
        
        <div class="section-card p-4 bg-white d-flex align-items-center justify-content-between">
          <div class="d-flex align-items-center gap-3">
            <div class="profile-avatar-circle text-primary-custom d-flex align-items-center justify-content-center">
              <i class="bi bi-stethoscope fs-2"></i>
            </div>
            <div>
              <h4 class="fw-bold text-dark mb-1">Dr. {{ medico.nomeCompleto }}</h4>
              <p class="text-primary-custom fw-semibold small mb-1">{{ medico.especialidade }}</p>
              <small class="text-muted">CRM: {{ medico.crm }} | Ativo desde Janeiro de 2024</small>
            </div>
          </div>
          <button class="btn btn-outline-secondary-custom px-3 py-2 rounded-3 fw-bold btn-sm">
            Alterar Foto
          </button>
        </div>

        <div class="section-card p-4 bg-white">
          <div class="section-header mb-4">
            <h5 class="fw-bold text-dark mb-1"><i class="bi bi-person me-2"></i>Dados Pessoais</h5>
            <p class="text-muted small mb-0">Suas informações básicas de cadastro</p>
          </div>
          
          <div class="row g-3">
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">Nome Completo</label>
              <input type="text" class="form-control rounded-3" v-model="medico.nomeCompleto" />
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">CRM</label>
              <input type="text" class="form-control rounded-3" v-model="medico.crm" disabled />
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">E-mail</label>
              <input type="email" class="form-control rounded-3" v-model="medico.email" />
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">Telefone</label>
              <input type="text" class="form-control rounded-3" v-model="medico.telefone" />
            </div>
            <div class="col-12">
              <label class="form-label text-muted small fw-semibold">Endereço do Consultório</label>
              <input type="text" class="form-control rounded-3" v-model="medico.endereco" />
            </div>
          </div>
        </div>

        <div class="section-card p-4 bg-white">
          <div class="section-header mb-4">
            <h5 class="fw-bold text-dark mb-1"><i class="bi bi-briefcase me-2"></i>Informações Profissionais</h5>
            <p class="text-muted small mb-0">Dados exibidos no seu perfil público</p>
          </div>

          <div class="row g-3">
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">Especialidade</label>
              <select class="form-select rounded-3" v-model="medico.especialidade">
                <option value="Cardiologia">Cardiologia</option>
                <option value="Clínica Geral">Clínica Geral</option>
                <option value="Pediatria">Pediatria</option>
              </select>
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">Valor da Consulta (R$)</label>
              <input type="number" class="form-control rounded-3" v-model="medico.valorConsulta" />
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">Duração Padrão da Consulta</label>
              <select class="form-select rounded-3" v-model="medico.duracaoConsulta">
                <option value="20 minutos">20 minutos</option>
                <option value="30 minutos">30 minutos</option>
                <option value="45 minutos">45 minutos</option>
                <option value="1 hora">1 hora</option>
              </select>
            </div>
            <div class="col-12">
              <label class="form-label text-muted small fw-semibold">Sobre Você</label>
              <textarea class="form-control rounded-3" rows="3" v-model="medico.sobre"></textarea>
            </div>
          </div>
        </div>

        <div class="section-card p-4 bg-white">
          <div class="section-header mb-4">
            <h5 class="fw-bold text-dark mb-1"><i class="bi bi-mortarboard me-2"></i>Formação Acadêmica</h5>
            <p class="text-muted small mb-0">Informações sobre sua formação e especializações</p>
          </div>
          <div class="col-12">
            <label class="form-label text-muted small fw-semibold">Formação e Especializações</label>
            <textarea class="form-control rounded-3 font-monospace" rows="4" v-model="medico.formacao"></textarea>
          </div>
        </div>

        <div class="section-card p-4 bg-white">
          <div class="section-header mb-4">
            <h5 class="fw-bold text-dark mb-1"><i class="bi bi-shield-check me-2"></i>Segurança</h5>
            <p class="text-muted small mb-0">Configurações de segurança da conta</p>
          </div>
          
          <div class="d-flex justify-content-between align-items-center py-2 border-bottom mb-3">
            <div>
              <h6 class="fw-bold text-dark mb-1 small">Alterar Senha</h6>
              <p class="text-muted small mb-0">Atualize sua senha de acesso</p>
            </div>
            <button class="btn btn-outline-secondary-custom btn-sm px-3 rounded-3 fw-semibold">Alterar</button>
          </div>

          <div class="d-flex justify-content-between align-items-center py-2">
            <div>
              <h6 class="fw-bold text-dark mb-1 small">Autenticação de Dois Fatores</h6>
              <p class="text-muted small mb-0">Adicione uma camada extra de segurança</p>
            </div>
            <button class="btn btn-outline-secondary-custom btn-sm px-3 rounded-3 fw-semibold">Configurar</button>
          </div>
        </div>

        <div class="section-card p-4 bg-white mb-4">
          <div class="section-header mb-4">
            <h5 class="fw-bold text-dark mb-1"><i class="bi bi-bell me-2"></i>Preferências de Notificação</h5>
            <p class="text-muted small mb-0">Configure como deseja receber alertas e lembretes</p>
          </div>

          <div class="d-flex justify-content-between align-items-center py-2 border-bottom mb-3">
            <div>
              <h6 class="fw-bold text-dark mb-1 small">Notificações por E-mail</h6>
              <p class="text-muted small mb-0">Receber alertas por e-mail</p>
            </div>
            <div class="form-check form-switch fs-5">
              <input class="form-check-input custom-switch" type="checkbox" v-model="medico.notificarEmail" checked>
            </div>
          </div>

          <div class="d-flex justify-content-between align-items-center py-2">
            <div>
              <h6 class="fw-bold text-dark mb-1 small">Notificações por SMS</h6>
              <p class="text-muted small mb-0">Receber alertas por mensagem de texto</p>
            </div>
            <div class="form-check form-switch fs-5">
              <input class="form-check-input custom-switch" type="checkbox" v-model="medico.notificarSms" checked>
            </div>
          </div>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import SidebarMedicoComp from '../components/doctor/SidebarDoctorComp.vue';

const medico = ref({
  nomeCompleto: 'Dr. Carlos Mendes',
  crm: '123456-SP',
  email: 'carlos.mendes@medconnect.com',
  telefone: '(11) 99999-9999',
  endereco: 'Av. Paulista, 1000 - São Paulo, SP',
  especialidade: 'Cardiologia',
  valorConsulta: 250,
  duracaoConsulta: '30 minutos',
  sobre: 'Médico cardiologista com mais de 15 anos de experiência. Especialista em arritmias cardíacas e insuficiência cardíaca.',
  formacao: 'Medicina - USP (2008)\nResidência em Cardiologia - InCor (2012)\nPós-graduação em Arritmias - Hospital Sírio-Libanês (2015)',
  notificarEmail: true,
  notificarSms: true
})

const buscarDadosPerfil = async () => {
  try {
    const token = localStorage.getItem('access_token')
    const response = await axios.get('http://localhost:8000/api/medicos/me/', {
      headers: { Authorization: `Bearer ${token}` }
    })
    medico.value = { ...medico.value, ...response.data }
  } catch (error) {
    console.error('Erro ao carregar dados do perfil:', error)
  }
}

onMounted(() => {
  buscarDadosPerfil()
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper {
  background-color: #f0f7f7;
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
}

.profile-container {
  max-width: 1000px; 
}

.section-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0 !important;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
}

.profile-avatar-circle {
  width: 70px;
  height: 70px;
  background-color: #eef7ff;
  border-radius: 50%;
  border: 1px solid #98DEF8;
}

.form-control, .form-select {
  border: 1px solid #cbd5e1;
  padding: 10px 14px;
  color: #334155;
  font-size: 0.95rem;
}
.form-control:focus, .form-select:focus {
  border-color: #0468BF;
  box-shadow: 0 0 0 3px rgba(4, 104, 191, 0.1);
}
.form-control:disabled {
  background-color: #f8fafc;
  color: #94a3b8;
}

.btn-outline-secondary-custom {
  border: 1px solid #cbd5e1;
  background-color: #ffffff;
  color: #475569;
  transition: all 0.2s;
}
.btn-outline-secondary-custom:hover {
  background-color: #f8fafc;
  border-color: #98DEF8;
  color: #0468BF;
}

.custom-switch:checked {
  background-color: #0468BF;
  border-color: #0468BF;
}

.text-primary-custom {
  color: #0468BF;
}
</style>