<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold mb-1 text-dark">Meu Perfil</h3>
        <p class="text-muted">Gerencie suas informações profissionais e preferências</p>
      </header>

      <div v-if="loadingPerfil" class="text-center py-5">
        <div class="spinner-border text-primary-custom" role="status"></div>
      </div>

      <div v-else class="d-flex flex-column gap-4 profile-container">
        
        <div v-if="sucesso" class="alert alert-success py-2 px-3 rounded-3 small border-0 shadow-sm animate__animated animate__fadeIn">
          <i class="bi bi-check-circle-fill me-2"></i> Perfil atualizado com sucesso!
        </div>
        <div v-if="erro" class="alert alert-danger py-2 px-3 rounded-3 small border-0 shadow-sm animate__animated animate__fadeIn">
          <i class="bi bi-exclamation-triangle-fill"></i> {{ erro }}
        </div>

        <div class="section-card p-4 bg-white d-flex align-items-center justify-content-between">
          <div class="d-flex align-items-center gap-3">
            <div class="profile-avatar-circle text-primary-custom d-flex align-items-center justify-content-center">
              <i class="bi bi-stethoscope fs-2"></i>
            </div>
            <div>
              <h4 class="fw-bold text-dark mb-1">Dr(a). {{ medico.NomeCompleto || 'Médico' }}</h4>
              <p class="text-primary-custom fw-semibold small mb-1">
                {{ medico.especialidades_detalhes?.map(e => e.nome).join(', ') || medico.Especialidades || 'Sem especialidade vinculada' }}
              </p>
              <small class="text-muted">CRM: {{ medico.Crm || 'Não informado' }} | Ativo no sistema</small>
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
              <input type="text" class="form-control rounded-3" v-model="medico.NomeCompleto" />
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">CRM</label>
              <input type="text" class="form-control rounded-3" v-model="medico.Crm" disabled />
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">E-mail</label>
              <input type="email" class="form-control rounded-3" v-model="medico.Email" />
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
              <label class="form-label text-muted small fw-semibold">Especialidade Principal (Filtro)</label>
              <select class="form-select rounded-3" v-model="medico.Especialidades">
                <option value="Cardiologia">Cardiologia</option>
                <option value="Clínica Geral">Clínica Geral</option>
                <option value="Pediatria">Pediatria</option>
              </select>
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">Valor da Consulta (R$)</label>
              <input type="number" class="form-control rounded-3" v-model="medico.ValorConsulta" />
            </div>
            <div class="col-md-6">
              <label class="form-label text-muted small fw-semibold">Duração Padrão da Consulta</label>
              <select class="form-select rounded-3" v-model="medico.DuracaoConsulta">
                <option value="20 minutos">20 minutos</option>
                <option value="30 minutos">30 minutos</option>
                <option value="45 minutos">45 minutos</option>
                <option value="1 hora">1 hora</option>
              </select>
            </div>
            <div class="col-12">
              <label class="form-label text-muted small fw-semibold">Sobre Você</label>
              <textarea class="form-control rounded-3" rows="3" v-model="medico.Sobre"></textarea>
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
            <textarea class="form-control rounded-3 font-monospace" rows="4" v-model="medico.Formacao"></textarea>
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
            <button type="button" class="btn btn-outline-secondary-custom btn-sm px-3 rounded-3 fw-semibold">Alterar</button>
          </div>
          <div class="d-flex justify-content-between align-items-center py-2">
            <div>
              <h6 class="fw-bold text-dark mb-1 small">Autenticação de Dois Fatores</h6>
              <p class="text-muted small mb-0">Adicione uma camada extra de segurança</p>
            </div>
            <button type="button" class="btn btn-outline-secondary-custom btn-sm px-3 rounded-3 fw-semibold">Configurar</button>
          </div>
        </div>

        <div class="section-card p-4 bg-white">
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
              <input class="form-check-input custom-switch" type="checkbox" v-model="medico.NotificarEmail">
            </div>
          </div>
          <div class="d-flex justify-content-between align-items-center py-2">
            <div>
              <h6 class="fw-bold text-dark mb-1 small">Notificações por SMS</h6>
              <p class="text-muted small mb-0">Receber alertas por mensagem de texto</p>
            </div>
            <div class="form-check form-switch fs-5">
              <input class="form-check-input custom-switch" type="checkbox" v-model="medico.NotificarSms">
            </div>
          </div>
        </div>

        <div class="section-card p-4 bg-white mb-4">
          <button 
            class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold w-100 d-flex align-items-center justify-content-center gap-2" 
            @click="salvarPerfil" 
            :disabled="salvando"
          >
            <span v-if="salvando" class="spinner-border spinner-border-sm" role="status"></span>
            <i v-else class="bi bi-save"></i> 
            {{ salvando ? 'Salvando Alterações...' : 'Salvar Alterações' }}
          </button>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import SidebarMedicoComp from '../components/doctor/SidebarDoctorComp.vue';
import { medicoService } from '../services/api.js'

const loadingPerfil = ref(true)
const salvando = ref(false)
const sucesso = ref(false)
const erro = ref('')

// Estrutura mapeada exatamente igual aos nomes de colunas do seu Django Admin
const medico = ref({
  NomeCompleto: '',
  Crm: '',
  Email: '',
  Telefone: '',
  Endereco: '',
  Especialidades: 'Cardiologia',
  ValorConsulta: 250,
  DuracaoConsulta: '30 minutos',
  Sobre: '',
  Formacao: '',
  NotificarEmail: true,
  NotificarSms: true,
  especialidades_detalhes: []
})

// Busca os dados da API
const buscarDadosPerfil = async () => {
  try {
    const res = await medicoService.getMe()
    console.log("Resposta bruta vinda do Django:", res.data)
    
    if (res && res.data) {
      // Cria uma unificação automática aceitando tanto chaves PascalCase quanto camelCase do servidor
      medico.value = {
        NomeCompleto: res.data.NomeCompleto || res.data.nomeCompleto || '',
        Crm: res.data.Crm || res.data.crm || res.data.Crm_id || '',
        Email: res.data.Email || res.data.email || '',
        Telefone: res.data.Telefone || res.data.telefone || '',
        Endereco: res.data.Endereco || res.data.endereco || '',
        Especialidades: res.data.Especialidades || res.data.especialidades || res.data.especialidade || 'Cardiologia',
        ValorConsulta: res.data.ValorConsulta || res.data.valorConsulta || 250,
        DuracaoConsulta: res.data.DuracaoConsulta || res.data.duracaoConsulta || '30 minutos',
        Sobre: res.data.Sobre || res.data.sobre || '',
        Formacao: res.data.Formacao || res.data.formacao || '',
        NotificarEmail: res.data.NotificarEmail !== undefined ? res.data.NotificarEmail : true,
        NotificarSms: res.data.NotificarSms !== undefined ? res.data.NotificarSms : true,
        especialidades_detalhes: res.data.especialidades_detalhes || []
      }
    }
  } catch (e) {
    erro.value = 'Erro ao carregar dados do perfil do servidor.'
    console.error('Erro detalhado no carregamento do perfil:', e)
  } finally {
    loadingPerfil.value = false
  }
}

// Envia os dados de volta ao Django respeitando o mapeamento estrito
const salvarPerfil = async () => {
  erro.value = ''
  sucesso.value = false
  salvando.value = true
  
  try {
    // Monta o objeto de payload respeitando as chaves com Letra Maiúscula exigidas pelo Django
    const payload = {
      NomeCompleto: medico.value.NomeCompleto,
      Email: medico.value.Email,
      Telefone: medico.value.Telefone,
      Endereco: medico.value.Endereco,
      Especialidades: medico.value.Especialidades,
      ValorConsulta: medico.value.ValorConsulta,
      DuracaoConsulta: medico.value.DuracaoConsulta,
      Sobre: medico.value.Sobre,
      Formacao: medico.value.Formacao,
      NotificarEmail: medico.value.NotificarEmail,
      NotificarSms: medico.value.NotificarSms
    }
    
    await medicoService.updateMe(payload)
    
    // Atualiza o cache local para a sidebar também refletir o novo nome na hora
    localStorage.setItem('user_name', medico.value.NomeCompleto)
    
    sucesso.value = true
    setTimeout(() => { sucesso.value = false }, 4000)
  } catch (e) {
    erro.value = 'Erro ao salvar. Verifique sua conexão ou se as chaves da API mudaram.'
    console.error('Erro detalhado ao tentar atualizar perfil:', e)
  } finally {
    salvando.value = false
  }
}

onMounted(buscarDadosPerfil)
</script>

<style scoped>
/* Mantido as regras CSS do seu layout impecáveis */
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #f0f7f7; min-height: 100vh; font-family: 'Inter', sans-serif; }
.profile-container { max-width: 1000px; }
.section-card { background: white; border-radius: 16px; border: 1px solid #e2e8f0 !important; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02); }
.profile-avatar-circle { width: 70px; height: 70px; background-color: #eef7ff; border-radius: 50%; border: 1px solid #98DEF8; }
.form-control, .form-select { border: 1px solid #cbd5e1; padding: 10px 14px; color: #334155; font-size: 0.95rem; }
.form-control:focus, .form-select:focus { border-color: #0468BF; box-shadow: 0 0 0 3px rgba(4, 104, 191, 0.1); }
.form-control:disabled { background-color: #f8fafc; color: #94a3b8; }
.btn-outline-secondary-custom { border: 1px solid #cbd5e1; background-color: #ffffff; color: #475569; transition: all 0.2s; }
.btn-outline-secondary-custom:hover { background-color: #f8fafc; border-color: #98DEF8; color: #0468BF; }
.btn-primary-custom { background-color: #0468BF; border: none; color: white; transition: background 0.3s ease; }
.btn-primary-custom:hover { background-color: #0060B4; color: white; }
.btn-primary-custom:disabled { background-color: #94a3b8; cursor: not-allowed; }
.custom-switch:checked { background-color: #0468BF; border-color: #0468BF; }
.text-primary-custom { color: #0468BF; }
</style>