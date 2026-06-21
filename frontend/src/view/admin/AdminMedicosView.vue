<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarAdminComp />
    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold text-dark mb-1">Gerenciar Médicos</h3>
          <p class="text-muted">Cadastre, edite e remova médicos do sistema</p>
        </div>
        <button class="btn btn-danger px-4 py-2 rounded-3 fw-bold d-flex align-items-center gap-2" @click="abrirModal()">
          <i class="bi bi-plus-lg"></i> Novo Médico
        </button>
      </header>

      <!-- Barra de busca -->
      <div class="section-card p-3 mb-4 d-flex gap-3">
        <div class="flex-grow-1 position-relative">
          <i class="bi bi-search position-absolute" style="left:14px;top:50%;transform:translateY(-50%);color:#94a3b8"></i>
          <input v-model="busca" class="form-control rounded-3 ps-5" placeholder="Buscar por nome ou CRM..." />
        </div>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-danger"></div>
      </div>

      <div v-else class="section-card overflow-hidden">
        <table class="table table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th class="px-4 py-3">Médico</th>
              <th>CRM</th>
              <th>E-mail</th>
              <th>Especialidades</th>
              <th class="text-end px-4">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="medicosFiltrados.length === 0">
              <td colspan="5" class="text-center py-4 text-muted">Nenhum médico encontrado</td>
            </tr>
            <tr v-for="m in medicosFiltrados" :key="m.id">
              <td class="px-4 py-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="avatar-sm bg-red-soft text-danger fw-bold rounded-circle d-flex align-items-center justify-content-center">{{ initials(m.nomeCompleto) }}</div>
                  <span class="fw-semibold text-dark">{{ m.nomeCompleto }}</span>
                </div>
              </td>
              <td class="font-monospace small text-muted">{{ m.crm }}</td>
              <td class="small text-muted">{{ m.email }}</td>
              <td>
                <span v-for="esp in (m.especialidades_detalhes || [])" :key="esp.id" class="badge bg-light text-muted border me-1 small">{{ esp.nome }}</span>
                <span v-if="!m.especialidades_detalhes?.length" class="text-muted small">—</span>
              </td>
              <td class="text-end px-4">
                <button class="btn btn-sm btn-outline-secondary rounded-3 me-1 px-3" @click="abrirModal(m)">
                  <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger rounded-3 px-3" @click="excluir(m)">
                  <i class="bi bi-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal -->
      <div v-if="modalAberto" class="modal-overlay d-flex align-items-center justify-content-center" @click.self="fecharModal">
        <div class="modal-card p-4">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h5 class="fw-bold mb-0">{{ editando ? 'Editar Médico' : 'Novo Médico' }}</h5>
            <button class="btn btn-sm btn-outline-secondary rounded-circle" @click="fecharModal"><i class="bi bi-x"></i></button>
          </div>

          <div v-if="erroModal" class="alert alert-danger py-2 small mb-3">{{ erroModal }}</div>

          <div class="row g-3">
            <div class="col-12">
              <label class="form-label">Nome Completo *</label>
              <input v-model="form.nomeCompleto" class="form-control rounded-3" placeholder="Dr. Nome Completo" />
            </div>
            <div class="col-md-6">
              <label class="form-label">CRM *</label>
              <input v-model="form.crm" class="form-control rounded-3" placeholder="CRM/SP 123456" :disabled="editando" />
            </div>
            <div class="col-md-6">
              <label class="form-label">E-mail *</label>
              <input v-model="form.email" type="email" class="form-control rounded-3" placeholder="email@dominio.com" />
            </div>
            <div v-if="!editando" class="col-12">
              <label class="form-label">Senha *</label>
              <input v-model="form.password" type="password" class="form-control rounded-3" placeholder="Senha de acesso" />
            </div>
          </div>

          <div class="d-flex gap-2 mt-4">
            <button class="btn btn-danger flex-grow-1 rounded-3 fw-bold" @click="salvar" :disabled="salvando">
              <span v-if="salvando" class="spinner-border spinner-border-sm me-2"></span>
              {{ salvando ? 'Salvando...' : (editando ? 'Salvar Alterações' : 'Cadastrar Médico') }}
            </button>
            <button class="btn btn-outline-secondary rounded-3 px-4" @click="fecharModal">Cancelar</button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, reactive, onMounted } from 'vue'
import SidebarAdminComp from '../../components/admin/SidebarAdminComp.vue'
import { medicoService } from '../../services/api.js'

const loading = ref(true)
const salvando = ref(false)
const medicos = ref([])
const busca = ref('')
const modalAberto = ref(false)
const editando = ref(null)
const erroModal = ref('')

const form = reactive({ nomeCompleto: '', crm: '', email: '', password: '', especialidades_ids: [] })

const medicosFiltrados = computed(() => {
  if (!busca.value) return medicos.value
  const b = busca.value.toLowerCase()
  return medicos.value.filter(m => m.nomeCompleto?.toLowerCase().includes(b) || m.crm?.toLowerCase().includes(b))
})

const initials = (nome) => nome ? nome.split(' ').filter(n=>n.length>0).slice(0,2).map(n=>n[0]).join('') : '?'

const carregarMedicos = async () => {
  loading.value = true
  try { const res = await medicoService.listar(); medicos.value = res.data }
  catch (e) { console.error(e) }
  finally { loading.value = false }
}

const abrirModal = (m = null) => {
  erroModal.value = ''
  editando.value = m
  if (m) {
    form.nomeCompleto = m.nomeCompleto
    form.crm = m.crm
    form.email = m.email
    form.password = ''
  } else {
    Object.assign(form, { nomeCompleto: '', crm: '', email: '', password: '', especialidades_ids: [] })
  }
  modalAberto.value = true
}

const fecharModal = () => { modalAberto.value = false; editando.value = null }

const salvar = async () => {
  erroModal.value = ''
  if (!form.nomeCompleto || !form.email || (!editando.value && (!form.crm || !form.password))) {
    erroModal.value = 'Preencha todos os campos obrigatórios.'
    return
  }
  salvando.value = true
  try {
    if (editando.value) {
      await medicoService.atualizar(editando.value.id, { nomeCompleto: form.nomeCompleto, email: form.email })
    } else {
      await medicoService.criar({ nomeCompleto: form.nomeCompleto, crm: form.crm, email: form.email, password: form.password, especialidades_ids: [] })
    }
    fecharModal()
    await carregarMedicos()
  } catch (e) {
    erroModal.value = Object.entries(e.response?.data || {}).map(([k,v]) => `${k}: ${Array.isArray(v)?v.join(', '):v}`).join(' | ') || 'Erro ao salvar.'
  } finally { salvando.value = false }
}

const excluir = async (m) => {
  if (!confirm(`Excluir o médico "${m.nomeCompleto}"? Esta ação é irreversível.`)) return
  try { await medicoService.excluir(m.id); await carregarMedicos() }
  catch { alert('Erro ao excluir médico.') }
}

onMounted(carregarMedicos)
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #fff5f5; min-height: 100vh; }
.section-card { background: white; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.avatar-sm { width: 38px; height: 38px; min-width: 38px; font-size: 0.85rem; }
.bg-red-soft { background: #fee2e2; }
.form-label { font-size: 0.85rem; font-weight: 600; color: #1e293b; margin-bottom: 0.3rem; display: block; }
.form-control { border: 1.5px solid #e2e8f0; padding: 10px 14px; }
.form-control:focus { border-color: #dc2626; box-shadow: 0 0 0 3px rgba(220,38,38,0.1); }
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 1000; backdrop-filter: blur(2px); }
.modal-card { background: white; border-radius: 20px; width: 100%; max-width: 540px; box-shadow: 0 20px 60px rgba(0,0,0,0.2); max-height: 90vh; overflow-y: auto; }
</style>
