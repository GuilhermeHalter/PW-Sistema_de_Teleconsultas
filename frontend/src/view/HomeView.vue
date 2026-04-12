<template>
  <div class="container-fluid p-0 wrapper">
    <nav class="navbar navbar-expand-lg bg-white border-bottom py-3 px-4">
      <div class="container">
        <a class="navbar-brand fw-bold d-flex align-items-center gap-2" href="#">
          <div class="logo-t text-white bg-primary-custom d-flex align-items-center justify-content-center rounded">
            T
          </div>
          <span class="text-dark fs-5">Teleconsulta</span>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-between" id="nav">
          <ul class="navbar-nav mx-auto gap-3">
            <li class="nav-item"><a class="nav-link text-dark fw-medium" href="#">Início</a></li>
            <li class="nav-item"><a class="nav-link text-muted" href="#">Como Funciona</a></li>
            <li class="nav-item"><a class="nav-link text-muted" href="#">Serviços</a></li>
            <li class="nav-item"><a class="nav-link text-muted" href="#">Contato</a></li>
          </ul>
          <div class="d-flex align-items-center gap-3">
            <a href="#" class="text-dark text-decoration-none fw-medium">Entrar</a>
            <button class="btn btn-primary-custom rounded-pill px-4 py-2 fw-medium shadow-sm">
              Agendar Consulta
            </button>
          </div>
        </div>
      </div>
    </nav>

    <section class="container py-5 my-4">
      <div class="row align-items-center g-5">
        <div class="col-lg-6 pe-lg-5">
          <div class="badge-soft-primary d-inline-flex align-items-center gap-2 mb-4">
            <span class="dot bg-primary-custom rounded-circle"></span>
            Telemedicina de Qualidade
          </div>
          
          <h1 class="hero-title font-serif fw-bold text-dark mb-4">
            Sua consulta <br>
            médica, <span class="text-primary-custom fst-italic">online</span> e <br>
            sem complicações.
          </h1>
          
          <p class="text-muted fs-5 mb-5 pe-lg-5 lh-base">
            Agende, pague e acesse sua consulta com segurança em poucos cliques. Conectamos você aos melhores profissionais de saúde, no conforto da sua casa.
          </p>

          <div class="d-flex align-items-center gap-3 mb-5">
            <button class="btn btn-primary-custom rounded-pill px-4 py-3 fw-medium d-flex align-items-center gap-2">
              Comece Agora <i class="bi bi-arrow-right"></i>
            </button>
            <button class="btn btn-outline-secondary rounded-pill px-4 py-3 fw-medium border-light-subtle text-dark d-flex align-items-center gap-2 shadow-sm bg-white">
              <i class="bi bi-play-circle text-muted fs-5"></i> Como Funciona
            </button>
          </div>

          <div class="d-flex mt-4 pt-3 border-top w-75">
            <div class="pe-4 border-end">
              <h3 class="fw-bold text-dark mb-0">+50k</h3>
              <small class="text-muted">Pacientes atendidos</small>
            </div>
            <div class="px-4 border-end">
              <h3 class="fw-bold text-dark mb-0">+200</h3>
              <small class="text-muted">Médicos parceiros</small>
            </div>
            <div class="ps-4">
              <h3 class="fw-bold text-dark mb-0">4.9</h3>
              <small class="text-muted">Avaliação média</small>
            </div>
          </div>
        </div>

        <div class="col-lg-6 text-center position-relative mt-5 mt-lg-0">
          <div class="image-wrapper position-relative d-inline-block">
            <div class="bg-shape position-absolute rounded-4 bg-light"></div>
            <img class="img-fluid rounded-4 position-relative z-1 hero-img" src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80&w=800" alt="Médica sorrindo" />
            
            <div class="floating-card top-right position-absolute d-flex align-items-center gap-2 p-2 px-3 z-2">
              <div class="d-flex avatar-group">
                <div class="avatar rounded-circle bg-primary-subtle"></div>
                <div class="avatar rounded-circle bg-info-subtle"></div>
                <div class="avatar rounded-circle bg-success-subtle"></div>
              </div>
              <small class="text-muted fw-medium" style="font-size: 0.7rem;">+1.2k online agora</small>
            </div>

            <div class="floating-card bottom-left position-absolute d-flex align-items-center p-3 pe-4 z-2">
              <div class="icon-circle bg-success-subtle text-success rounded-circle d-flex justify-content-center align-items-center me-3">
                <i class="bi bi-check-circle-fill fs-5"></i>
              </div>
              <div class="text-start">
                <h6 class="mb-0 fw-bold fs-6 text-dark">Consulta Confirmada</h6>
                <small class="text-muted" style="font-size: 0.8rem;">Dr. Maria Silva • 14:00</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="container py-5 my-5">
      <div class="mb-5">
        <small class="text-primary-custom fw-bold text-uppercase tracking-wide">Como Funciona</small>
        <h2 class="font-serif fw-bold text-dark mt-2 display-6 w-50">Atendimento médico simplificado para sua vida</h2>
      </div>

      <div class="row g-4 mt-2">
        <div class="col-md-3" v-for="(s, i) in steps" :key="i">
          <div class="step-number font-serif text-muted opacity-25 display-3 mb-2">{{ s.number }}</div>
          <div class="d-flex align-items-center gap-2 mb-3">
            <div class="step-icon bg-primary-subtle text-primary-custom rounded d-flex align-items-center justify-content-center">
              <i :class="s.icon"></i>
            </div>
            <h6 class="fw-bold text-dark mb-0">{{ s.title }}</h6>
          </div>
          <p class="text-muted small lh-lg pe-3">{{ s.desc }}</p>
        </div>
      </div>
    </section>

    <section class="container py-5 my-5">
      <div class="d-flex justify-content-between align-items-end mb-5">
        <div>
          <small class="text-primary-custom fw-bold text-uppercase tracking-wide">Especialidades</small>
          <h2 class="font-serif fw-bold text-dark mt-2 display-6">Encontre o especialista ideal para você</h2>
        </div>
        <button class="btn btn-outline-secondary bg-white border-light-subtle rounded-pill px-4 py-2 text-dark shadow-sm fw-medium d-flex align-items-center gap-2">
          Ver todas as especialidades <i class="bi bi-arrow-up-right text-muted"></i>
        </button>
      </div>

      <div class="row g-4">
        <div class="col-md-4" v-for="s in services" :key="s.title">
          <div class="card h-100 shadow-sm border-0 rounded-4 p-2 specialty-card cursor-pointer">
            <div class="card-body d-flex flex-column">
              <div class="d-flex justify-content-between align-items-start mb-3">
                <h5 class="card-title fw-bold text-dark mb-0">{{ s.title }}</h5>
                <i class="bi bi-arrow-up-right text-muted"></i>
              </div>
              <p class="card-text text-muted small lh-lg mb-4">{{ s.desc }}</p>
              
              <div class="mt-auto">
                <hr class="text-muted opacity-10">
                <span class="text-muted small">A partir de <strong class="text-dark fw-bold">{{ s.price }}</strong></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="container py-5 mb-5">
      <div class="bg-black text-white text-center rounded-5 px-4 py-5 shadow-lg cta-banner">
        <div class="py-4">
          <h2 class="font-serif fw-bold mb-3 display-4">Pronto para cuidar<br>da sua saúde?</h2>
          <p class="text-light mb-5 fs-5 text-opacity-75">Comece agora mesmo sua jornada de cuidado com a saúde. Agende sua<br>primeira consulta em menos de 2 minutos.</p>
          <div class="d-flex justify-content-center gap-3">
            <button class="btn bg-white text-dark rounded-pill px-4 py-3 fw-bold d-flex align-items-center gap-2 shadow">
              Agendar Consulta Agora <i class="bi bi-arrow-right"></i>
            </button>
            <button class="btn btn-outline-light rounded-pill px-4 py-3 fw-bold border-2 opacity-75 hover-opacity-100">
              Falar com Atendente
            </button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const services = [
  { title: 'Clínico Geral', desc: 'Consultas para avaliação de saúde geral, orientações e encaminhamentos.', price: 'R$ 89' },
  { title: 'Dermatologia', desc: 'Cuidados com a pele, cabelos e unhas. Diagnósticos e tratamentos especializados.', price: 'R$ 149' },
  { title: 'Psicologia', desc: 'Acompanhamento psicológico e terapia online com profissionais qualificados.', price: 'R$ 120' },
  { title: 'Nutrição', desc: 'Planos alimentares personalizados e acompanhamento nutricional completo.', price: 'R$ 99' },
  { title: 'Cardiologia', desc: 'Avaliação cardiovascular, orientações preventivas e acompanhamento.', price: 'R$ 180' },
  { title: 'Pediatria', desc: 'Cuidados especializados para a saúde de crianças e adolescentes.', price: 'R$ 130' }
]

const steps = [
  { number: '01', icon: 'bi bi-calendar-event', title: 'Agendamento Fácil', desc: 'Escolha o horário que melhor se encaixa na sua rotina. Disponibilidade 24 horas por dia, 7 dias por semana.' },
  { number: '02', icon: 'bi bi-camera-video', title: 'Consulta por Vídeo', desc: 'Atendimento de qualidade através de chamada de vídeo segura e de alta definição, direto no seu celular ou computador.' },
  { number: '03', icon: 'bi bi-shield-lock', title: 'Privacidade Total', desc: 'Seus dados e consultas são protegidos com criptografia de ponta a ponta. Sigilo médico garantido.' },
  { number: '04', icon: 'bi bi-file-earmark-medical', title: 'Receitas Digitais', desc: 'Receba receitas e atestados digitais válidos em todo o Brasil, diretamente no seu e-mail.' }
]
</script>

<style>
/* Importando fontes modernas parecidas com o design */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap');
/* Importando os ícones do Bootstrap */
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

:root {
  --primary-color: #0077B6;
  --bg-color: #FAFAFC;
}

body { 
  background-color: var(--bg-color);
  font-family: 'DM Sans', sans-serif;
}

.font-serif {
  font-family: 'Playfair Display', serif;
}

.text-primary-custom { color: var(--primary-color) !important; }
.bg-primary-custom { background-color: var(--primary-color) !important; }

.btn-primary-custom {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
  color: #fff;
}
.btn-primary-custom:hover {
  background-color: #005f92;
  color: #fff;
}

.logo-t {
  width: 28px;
  height: 28px;
  font-size: 14px;
}

.badge-soft-primary {
  background-color: #e8f4f8;
  color: var(--primary-color);
  font-weight: 600;
  font-size: 0.85rem;
  padding: 0.5rem 1rem;
  border-radius: 50px;
}
.badge-soft-primary .dot {
  width: 8px;
  height: 8px;
}

.hero-title {
  font-size: 4rem;
  line-height: 1.1;
  letter-spacing: -1px;
}

.hero-img {
  width: 85%;
  object-fit: cover;
  aspect-ratio: 4/5;
}

.bg-shape {
  width: 90%;
  height: 90%;
  top: 5%;
  right: 0;
  z-index: 0;
}

.floating-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}

.floating-card.bottom-left {
  bottom: 8%;
  left: -5%;
}

.floating-card.top-right {
  top: 8%;
  right: 5%;
  border-radius: 50px;
}

.avatar-group .avatar {
  width: 20px;
  height: 20px;
  border: 2px solid #fff;
  margin-left: -8px;
}
.avatar-group .avatar:first-child { margin-left: 0; }

.icon-circle {
  width: 44px;
  height: 44px;
}

.tracking-wide {
  letter-spacing: 1.5px;
}

.step-icon {
  width: 32px;
  height: 32px;
  font-size: 1.1rem;
}

.specialty-card {
  transition: transform 0.2s, box-shadow 0.2s;
  border: 1px solid rgba(0,0,0,0.03) !important;
}
.specialty-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0,0,0,0.06) !important;
}

.cta-banner {
  background-image: radial-gradient(circle at top right, #1a1a1a, #000000);
}
.cursor-pointer { cursor: pointer; }
.hover-opacity-100:hover { opacity: 1 !important; }
</style>