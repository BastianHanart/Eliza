import React, { useState } from 'react';
import './index.css';
import vetImg from './assets/veterinaire.svg'; 

const App = () => {
  const [activeIndex, setActiveIndex] = useState(null);

  const questions = [
    {
      q: "Est-ce que VetBot remplace un vétérinaire ?",
      a: "Non, VetBot est un outil d'assistance et de conseil. Il ne remplace en aucun cas l'examen physique et le diagnostic d'un vétérinaire professionnel."
    },
    {
      q: "Quels types de symptômes VetBot peut-il analyser ?",
      a: "VetBot peut analyser des symptômes courants comme la boiterie, les problèmes digestifs, cutanés ou les changements de comportement."
    },
    {
      q: "Quelle est la précision de VetBot ?",
      a: "Notre IA est entraînée sur des milliers de cas vétérinaires, offrant une analyse fiable pour orienter l'urgence de la situation."
    },
    {
      q: "VetBot est-il gratuit ?",
      a: "Oui, les fonctions de base et l'analyse de premier niveau sont totalement gratuites sur Discord."
    },
    {
      q: "De quelles informations VetBot a-t-il besoin ?",
      a: "Il suffit d'indiquer l'espèce, la race, l'âge approximatif et de décrire les symptômes observés de la manière la plus précise possible."
    }
  ];

  return (
    <div className="container">
      {/* header/haut de page*/}
      <header className="hero">
        <div className="hero-content">
          <span className="badge">🤖 Assistant de santé animale IA</span>
          <h1>VetBot</h1>
          <p className="hero-desc">
            Des conseils instantanés propulsés par l'IA pour la santé de votre animal, 
            directement dans Discord.
          </p>
          <a 
            href="https://discord.com/oauth2/authorize?client_id=1488182236233859173" 
            className="btn-discord" 
            target="_blank" 
            rel="noopener noreferrer"
            style={{ textDecoration: 'none', display: 'inline-block' }}
          >
            Ajouter à Discord
          </a>
        </div>
        <div className="hero-image">
          <div className="img-card">
            <img src={vetImg} alt="Illustration VetBot" />
            <div className="analysis-notif">
              <span className="dot"></span>
              <p>Analyse VetBot : Recommandation prête en 2s</p>
            </div>
          </div>
        </div>
      </header>

      {/* -comment sa marche*/}
      <section className="section">
        <h2 className="section-title">Comment ça marche</h2>
        <p className="section-subtitle">Trois étapes simples pour votre tranquillité d'esprit</p>
        <div className="steps-grid">
          <div className="card">
            <div className="icon-circle">🐾</div>
            <h3>1. Partagez la race & symptômes</h3>
            <p>Indiquez à VetBot la race de votre animal et les symptômes que vous remarquez.</p>
          </div>
          <div className="card">
            <div className="icon-circle">💬</div>
            <h3>2. L'IA analyse instantanément</h3>
            <p>Notre IA traite les informations en utilisant des connaissances vétérinaires.</p>
          </div>
          <div className="card">
            <div className="icon-circle">🩺</div>
            <h3>3. Obtenez des conseils clairs</h3>
            <p>Recevez des recommandations sur l'urgence d'une visite chez le vétérinaire.</p>
          </div>
        </div>
      </section>

      {/* information */}
      <section className="section">
        <h2 className="section-title">Tout ce dont vous avez besoin</h2>
        <p className="section-subtitle">Une assistance complète pour la santé de vos animaux à portée de main</p>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feat-icon">✨</div>
            <h3>Analyse des symptômes par l'IA</h3>
            <p>IA avancée formée sur des données vétérinaires pour évaluer les symptômes avec précision.</p>
          </div>
          <div className="feature-card">
            <div className="feat-icon">🕒</div>
            <h3>Réponses instantanées</h3>
            <p>Obtenez des conseils en quelques secondes, pas en quelques heures. Pas d'attente.</p>
          </div>
          <div className="feature-card">
            <div className="feat-icon">📱</div>
            <h3>Fonctionne dans Discord</h3>
            <p>Accédez à VetBot directement dans votre serveur Discord. Pas besoin de changer d'app.</p>
          </div>
          <div className="feature-card">
            <div className="feat-icon">⚠️</div>
            <h3>Système d'alerte vétérinaire</h3>
            <p>Des recommandations claires lorsqu'une prise en charge professionnelle est urgente.</p>
          </div>
        </div>
      </section>

      {/* demo conversation */}
      <section className="section">
        <h2 className="section-title">Voyez-le en action</h2>
        <p className="section-subtitle">Une vraie conversation sur Discord</p>
        <div className="discord-container">
          <div className="discord-header"># sante-animale</div>
          <div className="discord-msg">
            <div className="avatar user-av">G</div>
            <div>
              <p className="dc-user">GOATier <span className="dc-time">14:34</span></p>
              <p className="dc-text">Mon golden retriever boite de la patte arrière et semble souffrir quand je la touche.</p>
            </div>
          </div>
          <div className="discord-msg">
            <div className="avatar bot-av">V</div>
            <div>
              <p className="dc-user">VetBot <span className="bot-tag">BOT</span> <span className="dc-time">14:34</span></p>
              <p className="dc-text">Je vais vous aider. Pourriez-vous me dire :<br/>1. Depuis combien de temps boite-t-elle ?<br/>2. Y a-t-il un gonflement ou de la chaleur ?</p>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ  */}
      <section className="section faq-section">
        <h2 className="section-title">Questions fréquemment posées</h2>
        <div className="faq-list">
          {questions.map((item, i) => (
            <div 
              key={i} 
              className={`faq-item ${activeIndex === i ? 'active' : ''}`}
              onClick={() => setActiveIndex(activeIndex === i ? null : i)}
            >
              <div className="faq-question">
                <span>{item.q}</span>
                <span className="plus">{activeIndex === i ? '-' : '+'}</span>
              </div>
              {activeIndex === i && (
                <div className="faq-answer">
                  <p>{item.a}</p>
                </div>
              )}
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default App;