import React from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const projects = [
  {
    title: 'Análise de Vendas - Power BI',
    description: 'Dashboard interativo mostrando tendências de vendas mensais, desempenho por região e análise de produtos mais vendidos.',
    link: '#',
    chartData: [
      { name: 'Jan', vendas: 4000 },
      { name: 'Fev', vendas: 3000 },
      { name: 'Mar', vendas: 5000 },
      { name: 'Abr', vendas: 4000 },
      { name: 'Mai', vendas: 6000 },
    ],
  },
  {
    title: 'Análise de Dados Financeiros - Python & Pandas',
    description: 'Projeto de limpeza e análise de dados financeiros para identificar padrões de despesas e oportunidades de economia.',
    link: '#',
    chartData: [
      { name: 'Q1', despesas: 2000 },
      { name: 'Q2', despesas: 2500 },
      { name: 'Q3', despesas: 1800 },
      { name: 'Q4', despesas: 3000 },
    ],
  },
  {
    title: 'Pesquisa de Satisfação - SQL & Data Studio',
    description: 'Análise de dados de pesquisa de satisfação de clientes, com insights sobre pontos fortes e áreas a melhorar.',
    link: '#',
    chartData: [
      { name: 'Positivo', respostas: 80 },
      { name: 'Neutro', respostas: 15 },
      { name: 'Negativo', respostas: 5 },
    ],
  },
];

export default function Portfolio() {
  return (
    <div className="p-8 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold text-center mb-8">Portfólio de Análise de Dados</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map((project, index) => (
          <Card key={index} className="shadow-lg">
            <CardContent className="p-4">
              <h2 className="text-xl font-semibold mb-2">{project.title}</h2>
              <p className="mb-4 text-gray-600">{project.description}</p>
              <div className="h-40">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={project.chartData}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey={Object.keys(project.chartData[0])[1]} fill="#4F46E5" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
              <Button className="mt-4 w-full" asChild>
                <a href={project.link} target="_blank" rel="noopener noreferrer">Ver Projeto</a>
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
