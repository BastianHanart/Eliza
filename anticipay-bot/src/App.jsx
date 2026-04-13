import React from 'react';
import './index.css';

const App = () => {
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
            <img src="https://cdn.discordapp.com/attachments/1488182685892350004/1493211840572952586/veterinary-doctor-doing-vaccination-for-dog-free-vector.png?ex=69de2565&is=69dcd3e5&hm=30a671da3e751f40d0b6a24ebad55bc71d4d846ef4d798e66f4574d1c407ddf5&" alt="Dachshund" />
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

      {/* infomation */}
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
            <div className="avatar user-av">U</div>
            <div>
              <p className="dc-user">Propriétaire42 <span className="dc-time">14:34</span></p>
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

      {/*question */}
      <section className="section faq-section">
        <h2 className="section-title">Questions fréquemment posées</h2>
        <div className="faq-list">
          {[
            "Est-ce que VetBot remplace un vétérinaire ?",
            "Quels types de symptômes VetBot peut-il analyser ?",
            "Quelle est la précision de VetBot ?",
            "VetBot est-il gratuit ?",
            "De quelles informations VetBot a-t-il besoin ?"
          ].map((q, i) => (
            <div key={i} className="faq-item">
              <span>{q}</span>
              <span className="plus">+</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default App;