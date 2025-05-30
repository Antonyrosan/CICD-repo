// app.js
const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.static('public'));
app.set('view engine', 'ejs');

// Static content
const data = {
  name: 'Rosan A',
  tagline: 'Aspiring DevOps Engineer',
  skills: ['AWS', 'CI/CD', 'Docker', 'Terraform'],
  projects: [
    {
      title: 'Database Migration to AWS',
      description: 'Migrated on-prem DB to RDS using Percona XtraBackup.',
    },
    {
      title: '3-Tier Architecture Deployment',
      description: 'Deployed full-stack app across web, app, and DB layers.',
    },
    {
      title: 'End-to-End CI/CD Pipeline',
      description: 'Set up GitHub Actions for automatic testing & deployment.',
    },
    {
      title: 'IaC Network Provisioning',
      description: 'Used Terraform to build VPC, subnets, gateways on AWS.',
    }
  ],
  contact: {
    email: 'rosan@example.com',
    github: 'https://github.com/rosan-a',
    linkedin: 'https://linkedin.com/in/rosan-a'
  }
};

// Routes
app.get('/', (req, res) => res.render('index', { data }));
app.get('/about', (req, res) => res.render('about', { data }));
app.get('/projects', (req, res) => res.render('projects', { data }));
app.get('/contact', (req, res) => res.render('contact', { data }));

// Start server
app.listen(port, () => {
  console.log(`🚀 Portfolio app listening at http://localhost:${port}`);
});
