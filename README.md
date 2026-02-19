# Sistema de Teleconsultas

## Situação Problema
Com o avanço da tecnologia e a crescente demanda por atendimentos médicos remotos, especialmente após a popularização da telemedicina, tornou-se evidente a necessidade de sistemas seguros, organizados e confiáveis para a realização de teleconsultas.

Atualmente, muitos profissionais da saúde enfrentam dificuldades na gestão de agendas, confirmação de pagamentos, organização de horários e controle de acesso às consultas online. Em diversos casos, o envio manual de links de videoconferência, a ausência de validação automática de pagamento e falhas na autenticação de usuários geram atrasos, cancelamentos, conflitos de horários e riscos à segurança das informações.

Além disso, pacientes frequentemente encontram problemas como falta de confirmação clara da consulta, insegurança no processo de pagamento e dificuldade de acesso ao link da chamada no momento do atendimento.

## Resumo da Solução

Sistema de Teleconsulta que permite o gerenciamento de médicos e seus horários de atendimento, oferecendo um fluxo completo de check-in do paciente com validação de pagamento. Após a confirmação, o sistema libera o link da chamada, garantindo controle de agenda, segurança no acesso e uma experiência organizada de atendimento médico online.

## Mapa Stakeholders

<img width="1687" height="986" alt="Stakeholders teleconsultas" src="https://github.com/user-attachments/assets/6cba5634-49aa-49a0-9ebd-118262c523bd" />

## Funcionalidades

- Cadastro e gerenciamento de médicos
- Definição de horários de atendimento
- Check-in do paciente com validação de pagamento
- Liberação automática do link da consulta após confirmação
- Controle de agenda e segurança nos atendimentos

## Regras de Negócios

**RN01 –** O sistema deve possuir dois perfis principais: Médico e Paciente.

**RN02 –** O cadastro de usuários deve exigir autenticação segura (e-mail e senha criptografada).

**RN03 –** Apenas médicos previamente cadastrados e ativos podem disponibilizar horários para consulta.

**RN04 –** O acesso às funcionalidades deve respeitar o nível de permissão de cada perfil.

**RN05 –** O médico pode cadastrar, editar e remover horários disponíveis para atendimento.

**RN06 –** Um horário só pode ser reservado por um único paciente.

**RN07 –** O sistema deve impedir dupla reserva do mesmo horário (controle de concorrência).

**RN08 –** Após a reserva, o horário deve ficar automaticamente indisponível na agenda pública.

**RN09 –** O paciente só poderá agendar uma consulta em horários previamente disponibilizados pelo médico.

**RN10 –** O agendamento só será confirmado após a validação do pagamento.

**RN11 –** Caso o pagamento não seja confirmado, o horário deve retornar automaticamente para disponível.

**RN12 –** O sistema deve gerar um identificador único para cada consulta agendada.

**RN13 –** O pagamento deve ser realizado por meio de integração com gateway externo (ex: Stripe/PayPal).

**RN14 –** A confirmação da consulta depende do retorno positivo da API de pagamento.

**RN15 –** O sistema deve registrar o status do pagamento (Pendente, Aprovado, Recusado, Estornado).

**RN16 –** Em caso de falha no pagamento, o paciente deve ser notificado imediatamente.

**RN17 –** O link da videochamada só deve ser gerado ou liberado após confirmação do pagamento.

**RN18 –** O link deve ser único por consulta e possuir controle de acesso autenticado.

**RN19 –** O acesso ao link deve estar disponível apenas dentro do intervalo de horário da consulta.

**RN20 –** Apenas médico e paciente vinculados à consulta podem acessar a sala virtual.

**RN21 –** O paciente pode cancelar a consulta até um prazo mínimo definido pelo sistema (ex: 24h antes).

**RN22 –** O médico pode cancelar a consulta, devendo o paciente ser notificado automaticamente.

**RN23 –** Em caso de cancelamento dentro das regras, o sistema deve permitir estorno automático conforme política definida.

**RN24 –** O horário cancelado deve retornar à agenda como disponível.

**RN25 –** O sistema deve utilizar autenticação via JWT para validação de sessão.

**RN26 –** Todas as requisições sensíveis devem exigir token válido.

**RN27 –** Dados sensíveis (informações pessoais e pagamentos) devem ser armazenados de forma criptografada.

**RN28 –** O sistema deve registrar logs de acesso às consultas para auditoria.

**RN29 –** O paciente deve receber confirmação automática após agendamento e pagamento aprovado.

**RN30 –** O médico deve ser notificado sobre novas consultas agendadas.

**RN31 –** O sistema deve enviar lembrete automático antes do horário da consulta.

**RN32 –** A consulta deve possuir os seguintes estados:

- Disponível
- Reservada
- Aguardando Pagamento
- Confirmada
- Cancelada
- Finalizada
  
**RN33 –** As transições entre estados devem respeitar o fluxo definido pelo sistema (máquina de estados).

## Requisitos Funcionais

RF001: Cadastro de Usuário
Descrição: O sistema deve permitir que usuários realizem cadastro informando nome completo, e-mail e senha para criação de conta na plataforma.
Usuários: Médico, Paciente

RF002: Autenticação de Usuário
Descrição: O sistema deve permitir que usuários autenticados acessem a plataforma por meio de login com e-mail e senha validados.
Usuários: Médico, Paciente

RF003: Gerenciamento de Perfil
Descrição: O sistema deve permitir que o usuário visualize e edite suas informações pessoais cadastradas.
Usuários: Médico, Paciente

RF004: Cadastro de Horários Disponíveis
Descrição: O sistema deve permitir que o médico cadastre, edite e remova horários disponíveis para atendimento.
Usuários: Médico

RF005: Visualização de Horários Disponíveis
Descrição: O sistema deve permitir que o paciente visualize os horários disponíveis de um médico para agendamento.
Usuários: Paciente

RF006: Agendamento de Consulta
Descrição: O sistema deve permitir que o paciente agende uma consulta selecionando médico, data e horário disponíveis.
Usuários: Paciente

RF007: Integração com Sistema de Pagamento
Descrição: O sistema deve integrar-se a um gateway de pagamento para processar o pagamento da consulta no momento do agendamento.
Usuários: Paciente

RF008: Validação Automática de Pagamento
Descrição: O sistema deve validar automaticamente a confirmação do pagamento antes de confirmar o agendamento da consulta.
Usuários: Paciente, Médico

RF009: Confirmação de Consulta
Descrição: O sistema deve confirmar automaticamente a consulta após a validação do pagamento e notificar as partes envolvidas.
Usuários: Médico, Paciente

RF010: Geração de Link Seguro para Teleconsulta
Descrição: O sistema deve gerar um link exclusivo e seguro para cada consulta confirmada.
Usuários: Médico, Paciente

RF011: Controle de Acesso à Consulta
Descrição: O sistema deve permitir acesso ao link da teleconsulta apenas aos usuários autenticados e vinculados à consulta.
Usuários: Médico, Paciente

RF012: Cancelamento de Consulta
Descrição: O sistema deve permitir o cancelamento da consulta, registrando o status e aplicando regras definidas pela plataforma.
Usuários: Médico, Paciente

RF013: Histórico de Consultas
Descrição: O sistema deve permitir que usuários visualizem o histórico de consultas realizadas e agendadas.
Usuários: Médico, Paciente

## Requisitos Não Funcionais

RNF001: O sistema deve garantir autenticação segura utilizando criptografia de senhas e tokens de acesso.

RNF002: O sistema deve utilizar protocolo HTTPS para garantir a confidencialidade e integridade dos dados trafegados.

RNF003: O sistema deve possuir controle de acesso baseado em perfis (Médico e Paciente).

RNF004: O tempo de resposta das requisições críticas (login, agendamento, confirmação de pagamento) não deve ultrapassar 3 segundos em condições normais de uso.

RNF005: O sistema deve registrar logs de acesso e operações críticas para auditoria e rastreabilidade.

RNF006: O sistema deve permitir escalabilidade horizontal para suportar aumento no número de usuários simultâneos.

RNF007: O sistema deve garantir integridade transacional no processo de agendamento e pagamento.

RNF008: A interface deve ser responsiva, permitindo uso adequado em dispositivos desktop, tablet e smartphone.

RNF009: O sistema deve garantir backup periódico do banco de dados.

RNF010: O sistema deve permitir manutenção evolutiva e corretiva sem comprometer a integridade dos dados existentes.

RNF011: O sistema deve possuir validação de dados tanto no front-end quanto no back-end.

RNF012: O sistema deve ser compatível com os principais navegadores modernos (Chrome, Firefox, Edge).

## Definição de Arquitetura

- Arquitetura Client-Server

- Arquitetura Monolítica em Camadas (Layers)

- Padrão MVC (MTV no Django)

- Comunicação via REST API

## Padrões de Projeto Aplicados

### 1. MVC (Arquitetural)

Separa responsabilidades entre:

- Model (dados)

- View (API)

- Controller (fluxo)

Objetivo: modularidade e manutenção facilitada.

### 2. Strategy Pattern

Aplicado para múltiplos gateways de pagamento.

- Interface PaymentStrategy

- Implementações: StripeStrategy / PayPalStrategy

Permite extensão sem modificar código existente (OCP – SOLID).

### 3. Factory Pattern

Responsável por instanciar dinamicamente a estratégia de pagamento.

Reduz acoplamento com implementações concretas.

### 4. Observer Pattern

Utilizado na confirmação de pagamento:

Evento “Pagamento Confirmado” → libera link da consulta.

Desacopla módulo de pagamento do módulo de consulta.

### 5. Dependency Injection

Serviços são injetados nas camadas superiores.

Atende ao princípio:

- Dependency Inversion (SOLID)

Reduz acoplamento e melhora testabilidade.

## Tecnologias

- **Front-end**: Vue.js
    - Curva de aprendizado menor que React e Angular
    - Estrutura reativa simples e organizada
    - Excelente separação de responsabilidades (Componentização clara)
    - Ótimo equilíbrio entre performance e simplicidade
    - Integração fluida com APIs REST
      
- **Back-end**: Django (Python)
    - Framework robusto e maduro
    - Segurança nativa (CSRF, ORM seguro, autenticação)
    - ORM integrado → rapidez no desenvolvimento
    - Estrutura organizada (MTV)
    - Excelente para APIs com Django REST Framework

- **Banco de Dados**: MySQL
    - Banco relacional consolidado
    - Alta confiabilidade
    - Excelente suporte no Django
    - Ideal para dados estruturados (usuários, consultas, pagamentos)
  
- **Autenticação:** JWT
    - Stateless
    - Ideal para SPA
    - Escalável
    - Facilita separação frontend/backend
      
- **Pagamento:** Stripe / PayPal
    - APIs maduras
    - Segurança certificada
    - Webhooks robustos
    - Documentação clara
    - Amplamente usados no mercado
      
- **Videochamada:** Jitsi
    - 100% grátis
    - Pode hospedar seu próprio servidor
    - Fácil integração via iframe

- **Testes**: Cypress
    - Testes end-to-end reais
    - Simula comportamento do usuário
    - Excelente integração com SPA
    - Feedback visual

# Diagramas:

## Caso de Uso

<img width="1423" height="1397" alt="PW-Teleconsulta drawio" src="https://github.com/user-attachments/assets/c069079a-0c58-4aa3-ae03-bff38eebecc5" />

## C4Model

<img width="936" height="645" alt="Captura de tela 2026-02-18 182407" src="https://github.com/user-attachments/assets/784c68d5-32c8-4350-b2ce-efd07bd5735c" />

<img width="936" height="645" alt="Captura de tela 2026-02-18 184847" src="https://github.com/user-attachments/assets/0c4376e6-42c9-4e4f-964d-0a0d14febb5d" />

<img width="1116" height="728" alt="Captura de tela 2026-02-19 115001" src="https://github.com/user-attachments/assets/8104da83-299d-4f0f-a6d5-6352dc423bd1" />



## UML

## Classe

