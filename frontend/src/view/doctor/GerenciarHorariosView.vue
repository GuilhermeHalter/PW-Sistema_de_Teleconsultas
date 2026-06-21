<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Gerenciar Horários</h3>
          <p class="text-muted">Configure seus dias e horários disponíveis para atendimento</p>
        </div>
        <div class="d-flex align-items-center gap-3">
          <div class="input-group input-group-sm shadow-sm rounded-3 overflow-hidden border">
            <span class="input-group-text bg-white border-0 text-muted"><i class="bi bi-clock"></i></span>
            <span class="input-group-text bg-white border-0 fw-bold small pe-1">Duração:</span>
            
            <select v-model="duracaoSelecionada" class="form-select border-0 fw-bold text-primary-custom" style="width: 100px;">
              <option :value="30">30 min</option>
              <option :value="45">45 min</option>
              <option :value="60">60 min</option>
            </select>
          </div>
          <button class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold shadow-sm d-flex align-items-center gap-2" @click="carregarHorarios">
            <i class="bi bi-arrow-clockwise"></i> Atualizar
          </button>
        </div>
      </header>

      <div class="row g-4 mb-4">
        <div class="col-md-6 col-lg-3">
          <div class="stat-card p-3 d-flex align-items-center gap-3 bg-white">
            <div class="icon-box-round bg-blue-soft text-blue-deep"><i class="bi bi-stopwatch"></i></div>
            <div>
              <h5 class="mb-0 fw-bold">{{ duracaoSelecionada }} min</h5>
              <p class="mb-0 text-muted small">Por consulta</p>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="stat-card p-3 d-flex align-items-center gap-3 bg-white">
            <div class="icon-box-round bg-cyan-soft text-cyan-deep"><i class="bi bi-calendar-check"></i></div>
            <div>
              <h5 class="mb-0 fw-bold">{{ totalDisponiveis }}</h5>
              <p class="mb-0 text-muted small">Slots Disponíveis</p>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="stat-card p-3 d-flex align-items-center gap-3 bg-white border-dashed">
            <div class="icon-box-round bg-light text-muted"><i class="bi bi-calendar3"></i></div>
            <div>
              <h5 class="mb-0 fw-bold">{{ totalReservados }}</h5>
              <p class="mb-0 text-muted small">Slots Reservados</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="section-card p-4 h-100 bg-white shadow-sm border">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0"><i class="bi bi-calendar3 me-2"></i>Selecione uma Data</h5>
              <div class="calendar-nav d-flex align-items-center gap-3">
                <button class="btn btn-sm btn-light rounded-circle" @click="mudarMes(-1)"><i class="bi bi-chevron-left"></i></button>
                <span class="fw-bold text-dark">{{ labelMesAno }}</span>
                <button class="btn btn-sm btn-light rounded-circle" @click="mudarMes(1)"><i class="bi bi-chevron-right"></i></button>
              </div>
            </div>

            <div v-if="loading" class="text-center py-5">
              <div class="spinner-border text-primary" role="status"></div>
            </div>

            <div v-else class="calendar-grid">
              <div class="weekday">Dom</div><div class="weekday">Seg</div><div class="weekday">Ter</div>
              <div class="weekday">Qua</div><div class="weekday">Qui</div><div class="weekday">Sex</div><div class="weekday">Sáb</div>
              
              <div v-for="empty in primeiroDiaSemana" :key="'empty-' + empty" class="day empty"></div>
              
              <div 
                v-for="dia in diasNoMes" 
                :key="dia" 
                class="day" 
                :class="{ 
                  'active': isDiaSelecionado(dia),
                  'has-slots': temHorarioNoDia(dia)
                }"
                @click="selecionarDia(dia)"
              >
                {{ dia }}
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="section-card p-4 h-100 bg-white shadow-sm border">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <div>
                <h5 class="fw-bold mb-1 text-dark"><i class="bi bi-clock-history me-2"></i>Horários Disponíveis</h5>
                <p class="text-muted small mb-0">Horários para {{ formatarDataExibicao }}</p>
              </div>
            </div>

            <div v-if="slotsDoDia.length === 0" class="text-center py-5 text-muted bg-light rounded-3 mb-3">
              <i class="bi bi-calendar-x fs-3 d-block mb-2"></i>
              Nenhum horário cadastrado para este dia.
            </div>

            <div class="slots-grid">
              <div 
                v-for="slot in slotsDoDia" 
                :key="slot.id" 
                class="slot-item position-relative group" 
                :class="{ 'active': slot.disponivel, 'reservado': !slot.disponivel }"
                :title="'Fim: ' + formatarHora(slot.data_hora_fim)"
              >
                {{ formatarHora(slot.data_hora_inicio) }} - {{ formatarHora(slot.data_hora_fim) }}
                
                <span 
                  v-if="slot.disponivel" 
                  class="badge-delete shadow-sm"
                  data-bs-toggle="modal"
                  data-bs-target="#modalConfirmarExclusao"
                  @click.stop="prepararExclusao(slot)"
                >
                  <i class="bi bi-x-circle-fill text-danger"></i>
                </span>
              </div>

              <button class="btn-add-slot py-2" data-bs-toggle="modal" data-bs-target="#modalNovoHorario">
                <i class="bi bi-plus-lg me-1"></i> Adicionar
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <div class="modal fade" id="modalNovoHorario" tabindex="-1" aria-labelledby="modalNovoHorarioLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow rounded-4">
          <div class="modal-header border-0 pb-0">
            <h5 class="modal-title fw-bold" id="modalNovoHorarioLabel"><i class="bi bi-plus-circle me-2 text-primary-custom"></i>Novo Horário</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" id="fecharModalBtn"></button>
          </div>
          <div class="modal-body py-4">
            <div class="mb-3">
              <label class="form-label text-muted small fw-semibold">Data e Hora de Início</label>
              <input type="datetime-local" class="form-control rounded-3" v-model="novoHorario.inicio" />
            </div>
            
            <div class="mb-3 bg-light p-3 rounded-3 border">
              <div class="text-muted small fw-semibold mb-1">Cálculo de Término Automático:</div>
              <div class="fw-bold text-dark d-flex align-items-center gap-2">
                <i class="bi bi-calculator text-primary-custom"></i>
                <span v-if="novoHorario.inicio">{{ textoFimCalculado }}</span>
                <span v-else class="text-muted font-monospace small">Aguardando hora de início...</span>
              </div>
            </div>

            <div v-if="erroForm" class="alert alert-danger py-2 small">{{ erroForm }}</div>
            <div v-if="sucessoForm" class="alert alert-success py-2 small">Horário adicionado com sucesso!</div>
          </div>
          <div class="modal-footer border-0 pt-0">
            <button type="button" class="btn btn-light rounded-3 fw-bold px-4" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-primary-custom rounded-3 fw-bold px-4" @click="adicionarHorario" :disabled="salvando">
              <span v-if="salvando" class="spinner-border spinner-border-sm me-2"></span>
              <span v-else><i class="bi bi-save me-2"></i>Salvar</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="modalConfirmarExclusao" tabindex="-1" aria-labelledby="modalConfirmarExclusaoLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-sm">
        <div class="modal-content border-0 shadow rounded-4 text-center">
          <div class="modal-body pt-4 pb-3">
            <div class="text-danger mb-3">
              <i class="bi bi-exclamation-triangle-fill fs-1"></i>
            </div>
            <h5 class="fw-bold text-dark mb-2">Excluir Horário?</h5>
            <p class="text-muted small px-2">
              Tem certeza que deseja remover o slot do dia 
              <strong v-if="slotParaExcluir">{{ formatarDataSlotExclusao }}</strong> 
              das 
              <strong v-if="slotParaExcluir">{{ formatarHora(slotParaExcluir.data_hora_inicio) }} às {{ formatarHora(slotParaExcluir.data_hora_fim) }}</strong>?
            </p>
            <div v-if="erroExclusao" class="alert alert-danger py-1 small mt-2 mb-0">{{ erroExclusao }}</div>
          </div>
          <div class="modal-footer border-0 d-flex justify-content-center gap-2 pb-4 pt-0">
            <button type="button" class="btn btn-light rounded-3 fw-bold px-3 py-2 text-muted small" data-bs-dismiss="modal" id="fecharModalExcluirBtn">
              Cancelar
            </button>
            <button type="button" class="btn btn-danger rounded-3 fw-bold px-3 py-2 small d-flex align-items-center gap-2" @click="confirmarExclusao" :disabled="excluindo">
              <span v-if="excluindo" class="spinner-border spinner-border-sm"></span>
              <span v-else><i class="bi bi-trash3"></i> Excluir</span>
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import SidebarMedicoComp from '../../components/doctor/SidebarDoctorComp.vue';
import { horarioService } from '../../services/api.js'

const loading = ref(true)
const salvando = ref(false)
const excluindo = ref(false)
const horarios = ref([])
const erroForm = ref('')
const erroExclusao = ref('')
const sucessoForm = ref(false)

const duracaoSelecionada = ref(30) 
const novoHorario = ref({ inicio: '' }) 
const slotParaExcluir = ref(null)

const dataAtualCalendario = ref(new Date()) 
const diaSelecionado = ref(new Date().getDate())

const obterDataValida = (stringISO) => {
  if (!stringISO) return null
  if (stringISO.includes('T')) {
    const [dataParte, horaParte] = stringISO.split('T')
    const [ano, mes, dia] = dataParte.split('-').map(Number)
    const [hora, minuto] = horaParte.split(':').map(Number)
    return new Date(ano, mes - 1, dia, hora, minuto)
  }
  return new Date(stringISO)
}

const dataFimCalculada = computed(() => {
  if (!novoHorario.value.inicio) return null
  const dataInicio = new Date(novoHorario.value.inicio)
  return new Date(dataInicio.getTime() + duracaoSelecionada.value * 60000)
})

const textoFimCalculado = computed(() => {
  if (!dataFimCalculada.value) return ''
  return dataFimCalculada.value.toLocaleString('pt-BR', { 
    day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' 
  })
})

const labelMesAno = computed(() => {
  return dataAtualCalendario.value.toLocaleString('pt-BR', { month: 'long', year: 'numeric' })
    .replace(/^\w/, (c) => c.toUpperCase())
})

const diasNoMes = computed(() => {
  const ano = dataAtualCalendario.value.getFullYear()
  const mes = dataAtualCalendario.value.getMonth()
  return new Date(ano, mes + 1, 0).getDate()
})

const primeiroDiaSemana = computed(() => {
  const ano = dataAtualCalendario.value.getFullYear()
  const mes = dataAtualCalendario.value.getMonth()
  return new Date(ano, mes, 1).getDay()
})

const formatarDataExibicao = computed(() => {
  const ano = dataAtualCalendario.value.getFullYear()
  const mes = dataAtualCalendario.value.getMonth()
  const dataCompleta = new Date(ano, mes, diaSelecionado.value)
  return dataCompleta.toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric' })
})

const formatarDataSlotExclusao = computed(() => {
  if (!slotParaExcluir.value) return ''
  const d = obterDataValida(slotParaExcluir.value.data_hora_inicio)
  return d ? d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' }) : ''
})

const totalDisponiveis = computed(() => horarios.value.filter(h => h.disponivel).length)
const totalReservados = computed(() => horarios.value.filter(h => !h.disponivel).length)

const slotsDoDia = computed(() => {
  return horarios.value.filter(h => {
    const dataHorario = obterDataValida(h.data_hora_inicio)
    if (!dataHorario) return false
    
    return dataHorario.getDate() === diaSelecionado.value &&
           dataHorario.getMonth() === dataAtualCalendario.value.getMonth() &&
           dataHorario.getFullYear() === dataAtualCalendario.value.getFullYear()
  }).sort((a, b) => new Date(a.data_hora_inicio) - new Date(b.data_hora_inicio))
})

const isDiaSelecionado = (dia) => dia === diaSelecionado.value

const temHorarioNoDia = (dia) => {
  return horarios.value.some(h => {
    const d = obterDataValida(h.data_hora_inicio)
    if (!d) return false
    return d.getDate() === dia && 
           d.getMonth() === dataAtualCalendario.value.getMonth() &&
           d.getFullYear() === dataAtualCalendario.value.getFullYear()
  })
}

const formatarHora = (isoString) => {
  const d = obterDataValida(isoString)
  if (!d) return ''
  return d.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
}

const selecionarDia = (dia) => {
  diaSelecionado.value = dia
}

const mudarMes = (direcao) => {
  const novoMes = dataAtualCalendario.value.getMonth() + direcao
  dataAtualCalendario.value = new Date(dataAtualCalendario.value.getFullYear(), novoMes, 1)
  diaSelecionado.value = 1 
}

const carregarHorarios = async () => {
  loading.value = true
  try {
    const res = await horarioService.listarMeus()
    if (Array.isArray(res.data)) {
      horarios.value = res.data
    } else if (res.data && Array.isArray(res.data.dados)) {
      horarios.value = res.data.dados 
    } else {
      horarios.value = []
    }
  } catch (e) {
    console.error('Erro ao buscar horários:', e)
    horarios.value = []
  } finally {
    loading.value = false
  }
}

const adicionarHorario = async () => {
  erroForm.value = ''
  sucessoForm.value = false

  if (!novoHorario.value.inicio) {
    erroForm.value = 'Selecione o horário de início.'
    return
  }

  const novaDataInicio = new Date(novoHorario.value.inicio)
  const novaDataFim = dataFimCalculada.value

  if (novaDataInicio < new Date()) {
    erroForm.value = 'Você não pode criar um slot em um horário que já passou.'
    return
  }

  for (const existente of horarios.value) {
    const inicioExistente = new Date(existente.data_hora_inicio)
    const fimExistente = new Date(existente.data_hora_fim)

    if (novaDataInicio < fimExistente && novaDataFim > inicioExistente) {
      erroForm.value = `Conflito de agenda! Esse horário choca com o slot já configurado das ${formatarHora(existente.data_hora_inicio)} às ${formatarHora(existente.data_hora_fim)}.`
      return
    }
  }

  salvando.value = true
  try {
    const offset = novaDataInicio.getTimezoneOffset() * 60000
    const isoInicioLocal = new Date(novaDataInicio.getTime() - offset).toISOString().slice(0, -1)
    const isoFimLocal = new Date(novaDataFim.getTime() - offset).toISOString().slice(0, -1)

    await horarioService.criar({
      data_hora_inicio: isoInicioLocal,
      data_hora_fim: isoFimLocal,
      disponivel: true
    })
    
    novoHorario.value = { inicio: '' }
    sucessoForm.value = true
    await carregarHorarios()
    
    setTimeout(() => { 
      sucessoForm.value = false
      const fecharBtn = document.getElementById('fecharModalBtn')
      if(fecharBtn) fecharBtn.click()
    }, 1200)
  } catch (e) {
    erroForm.value = 'Falha ao salvar. Verifique a comunicação com o servidor.'
  } finally {
    salvando.value = false
  }
}

// Guarda as informações do slot que será deletado e limpa erros antigos
const prepararExclusao = (slot) => {
  erroExclusao.value = ''
  slotParaExcluir.value = slot
}

// Executa a chamada assíncrona de deleção da API de forma segura
const confirmarExclusao = async () => {
  if (!slotParaExcluir.value) return
  
  excluindo.value = true
  erroExclusao.value = ''
  try {
    await horarioService.excluir(slotParaExcluir.value.id)
    await carregarHorarios()
    
    // Fecha o modal via gatilho nativo do Bootstrap após o sucesso
    const fecharBtn = document.getElementById('fecharModalExcluirBtn')
    if (fecharBtn) fecharBtn.click()
    slotParaExcluir.value = null
  } catch (e) {
    erroExclusao.value = 'Erro ao excluir o horário selecionado.'
  } finally {
    excluindo.value = false
  }
}

onMounted(carregarHorarios)
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #f0f7f7; min-height: 100vh; font-family: 'Inter', sans-serif; }
.stat-card { border-radius: 16px; border: 1px solid #e2e8f0; }
.icon-box-round { width: 42px; height: 42px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
.border-dashed { border-style: dashed !important; }
.section-card { border-radius: 16px; }
.calendar-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 10px; text-align: center; }
.weekday { font-weight: bold; color: #94a3b8; font-size: 0.85rem; padding-bottom: 10px; }
.day { aspect-ratio: 1; display: flex; align-items: center; justify-content: center; border-radius: 50%; cursor: pointer; font-weight: 500; color: #475569; font-size: 0.95rem; position: relative; transition: all 0.2s; }
.day:hover:not(.empty) { background-color: #f1f5f9; }
.day.active { background-color: #0468BF; color: white; font-weight: bold; box-shadow: 0 4px 8px rgba(4, 104, 191, 0.3); }
.day.has-slots::after { content: ''; position: absolute; bottom: 5px; width: 4px; height: 4px; background-color: #0468BF; border-radius: 50%; }
.day.active.has-slots::after { background-color: white; }
.slots-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
.slot-item { padding: 10px; text-align: center; border-radius: 8px; font-weight: 600; font-size: 0.85rem; cursor: pointer; transition: all 0.2s; }
.slot-item.active { background-color: #e6f6f4; border: 1px solid #2ec4b6; color: #2e7d32; }
.slot-item.reservado { background-color: #fef9f0; border: 1px solid #fde8c3; color: #f57c00; cursor: not-allowed; }
.slot-item:hover:not(.reservado) { transform: translateY(-2px); border-color: #0468BF; }
.badge-delete { position: absolute; top: -6px; right: -4px; display: none; font-size: 1rem; cursor: pointer; background: white; border-radius: 50%; }
.slot-item:hover .badge-delete { display: block; }
.btn-add-slot { border: 2px dashed #cbd5e1; background: transparent; border-radius: 8px; color: #64748b; font-weight: 600; font-size: 0.9rem; transition: all 0.2s; }
.btn-add-slot:hover { border-color: #0468BF; color: #0468BF; background-color: #eef7ff; }
.btn-primary-custom { background-color: #0468BF; border: none; color: white; transition: background 0.3s; }
.btn-primary-custom:hover { background-color: #0060B4; color: white; }
.btn-primary-custom:disabled { background-color: #94a3b8; }
.form-control { border: 1px solid #cbd5e1; padding: 10px 14px; }
.form-control:focus { border-color: #0468BF; box-shadow: 0 0 0 3px rgba(4,104,191,0.1); }
.text-primary-custom { color: #0468BF; }
.bg-blue-soft { background-color: #eef7ff; }
.text-blue-deep { color: #0468BF; }
.bg-cyan-soft { background-color: #DFF2F0; }
.text-cyan-deep { color: #0060B4; }
@media (max-width: 1400px) { .slots-grid { grid-template-columns: 1fr; } }
</style>