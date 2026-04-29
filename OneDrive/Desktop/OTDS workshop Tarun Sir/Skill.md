---
name: study-enhance
description: "Transform textbook content into an interactive, experiential learning journey. Use this skill whenever a student wants to engage with a textbook PDF, study a topic deeply, or learn through hands-on activities. Triggers on: help me study, make this interactive, I want to learn X, explain this chapter, teach me, or any uploaded textbook/academic PDF."
license: Complete terms in LICENSE.txt
---

## When to use this skill
Use this skill whenever a student wants to:
- Engage interactively with a textbook or academic PDF
- Understand a concept through visuals, demos, or hands-on labs
- Learn through projects, experiments, or real-world applications
- Get curated resources (videos, articles, papers) on a topic
- Study in a way that matches their learning style

## How to use this skill

### Step 1: Identify the learner
Before diving in, quickly assess:
- **Topic/subject** — what chapter or concept are we working with?
- **Learning style** — do they prefer visuals, hands-on code, reading, or discussion?
- **Goal** — are they exploring, preparing for an exam, or building something?

If unclear, ask one focused question before proceeding.

### Step 2: Choose the right learning format
Pick from these formats based on the topic and learner:

- `formats/codelab.md` — For programming, algorithms, or anything with runnable code
- `formats/visualization.md` — For math, physics, data, or spatial concepts
- `formats/project-lab.md` — For applied, build-something learning
- `formats/resource-map.md` — For curated YouTube videos, articles, and papers
- `formats/meme-explainer.md` — For humor-based memory hooks and concept memes
- `formats/experiment-demo.md` — For science concepts with demo walkthroughs

More than one format can be combined in a single session.

### Step 3: Deliver the experience
Follow the specific instructions in the chosen format file. Always:
1. **Start with a hook** — a question, surprising fact, or visual that grabs attention
2. **Build understanding progressively** — don't dump everything at once
3. **Prompt thinking** — ask "what do you think happens if...?" before revealing answers
4. **Reinforce with resources** — link YouTube videos, articles, or experiment demos where relevant
5. **End with a challenge** — a mini project, quiz question, or real-world application

## Learning Format Guidelines

### Codelabs
- Provide working, runnable code snippets with clear explanations
- Break into small steps with expected outputs shown
- Include a "try it yourself" challenge at the end

### Visualizations & Animations
- Use Claude artifacts to render graphs, diagrams, or simulations inline
- Explain what to look for in the visual before showing it
- Tie the visual back to the textbook concept explicitly

### Resource Maps
- Link YouTube videos with timestamps where possible
- Prefer official docs, university lectures, and reputable articles
- Add a one-line summary of why each resource is worth visiting

### Project Labs
- Frame as a real-world problem, not a textbook exercise
- Provide a clear brief: goal, constraints, starter material
- Offer hints progressively — don't hand over the solution

### Meme Explainers
- Use humor to encode the concept memorably
- Keep it accurate — the joke should reinforce, not distort, the idea
- Pair with a clean one-line summary of the actual concept

### Experiment Demos
- Walk through the experiment setup, prediction, result, and explanation
- Use video links or simulations where physical setup isn't possible
- Ask the student to predict the outcome before revealing it

## Personalization
Adapt tone and depth based on cues:
- **Beginner signals** (lots of questions, slow pace) → use analogies, simpler language, more visuals
- **Advanced signals** (technical vocabulary, asks "why") → go deeper, skip basics, link to papers
- **Visual learner** → lead with diagrams and animations
- **Hands-on learner** → lead with codelabs and project labs
- **Reader** → lead with curated articles and structured explanations

## Keywords
study, learn, textbook, chapter, explain, interactive, codelab, visualization, project, experiment, YouTube, resources, understand, concept, tutorial, lecture, notes, PDF
