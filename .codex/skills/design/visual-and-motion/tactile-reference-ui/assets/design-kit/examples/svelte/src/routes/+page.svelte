<script lang="ts">
  import { tick } from 'svelte';
  import {
    Theme, Surface, Button, Badge, Field, Switch, Tabs, MetricCard, Orb,
    FeatureCard, Sparkline, IntegrationMap, FileStack, Meter, Dialog,
    PosterCard, Shield, OnboardingCard, ActionLink, SiteHeader, AmbientBackdrop,
    MarketingHero, SectionHeading, ShowcaseCard, FrostedIcon, Reveal,
    MotionStage, TaskComposer, ProcessCard, DeviceFrame, MaterialObject,
    Accordion, SegmentedControl, InlineNotice, EmptyState, AvatarStack, Skeleton
  } from '@tactile-ui/svelte';
  import { directions, type Direction, type Atmosphere } from '@tactile-ui/tokens';

  let direction = $state<Direction>('meadow');
  const directionSelectId = $props.id();
  let texture = $state(true);
  let ambientMotion = $state(true);
  let dialogOpen = $state(false);
  let tab = $state('anatomy');
  let name = $state('');
  let nameError = $state('');
  let step = $state(1);
  let status = $state('All values in this gallery are illustrative.');
  let directionHeading: HTMLDivElement | undefined;
  let task = $state('Plan a weekend in Lisbon');
  let taskError = $state('');
  let outline = $state('');
  let fileFilter = $state('all');
  let previewMode = $state('overview');
  let loadingPreview = $state(false);
  const people = [{ id: 'maya', name: 'Maya Chen', initials: 'MC' }, { id: 'sam', name: 'Sam Rivera', initials: 'SR' }, { id: 'jo', name: 'Jo Miller', initials: 'JM' }, { id: 'leah', name: 'Leah Ahmed', initials: 'LA' }, { id: 'alex', name: 'Alex Kim', initials: 'AK' }];
  const preset = $derived(directions.find(item => item.id === direction)!);
  const nodes = [
    { id: 'notes', label: 'Notes', detail: 'Your working context', symbol: 'N' },
    { id: 'files', label: 'Files', detail: 'Source material', symbol: 'F' },
    { id: 'team', label: 'Team', detail: 'Shared decisions', symbol: 'T' },
    { id: 'publish', label: 'Exports', detail: 'Approved output', symbol: 'E' }
  ];
  const files = [
    { id: 'research', name: 'Research', detail: '12 sample files' },
    { id: 'assets', name: 'Assets', detail: '8 sample files' },
    { id: 'notes', name: 'Notes', detail: '3 sample files', kind: 'document' as const }
  ];
  const recipes: Record<Direction, { title: string; description: string; eyebrow: string; align: 'center' | 'split'; atmosphere?: Atmosphere }> = {
    porcelain: { title: 'Quiet surfaces. Clear intention.', description: 'A soft physical frame, restrained blue accents, and room for the work that matters.', eyebrow: 'A little space to think', align: 'split' },
    spectral: { title: 'Make room for possibility.', description: 'Blue light, lavender air, and one luminous focal point. A calm canvas for the next idea.', eyebrow: 'Light, with intention', align: 'center' },
    editorial: { title: 'Small details. A lasting impression.', description: 'Confident type, an open composition, and one warm physical detail make the story clear.', eyebrow: 'Thoughtfully made', align: 'split' },
    citrus: { title: 'Your ideas deserve a brighter future.', description: 'One clear view of your projects, plans, and next steps. Make room for the possibilities ahead.', eyebrow: 'A fresh perspective', align: 'center' },
    signal: { title: 'A clearer view of the work.', description: 'Dense information, deliberate hierarchy, and visible states. Every label has a useful job.', eyebrow: 'Focus on what matters', align: 'split' },
    connected: { title: 'Every connection has a purpose.', description: 'Bring working context together through fine paths, tactile nodes, and readable relationships.', eyebrow: 'Connected canvas', align: 'center', atmosphere: 'paths' },
    meadow: { title: 'Make room for a new idea.', description: 'A quiet invitation to gather your thoughts, connect your sources, and find a useful way forward.', eyebrow: 'A lighter way to begin', align: 'center', atmosphere: 'meadow' },
    equilibrium: { title: 'Where ideas find their balance.', description: 'Bring clarity to complex work through a considered structure, a steady rhythm, and room to think.', eyebrow: 'Structure with intention', align: 'center', atmosphere: 'contours' },
    systems: { title: 'The infrastructure behind a clearer day.', description: 'Bring your tools and working context together. See the connections, choose the next step, and keep moving.', eyebrow: 'A connected foundation', align: 'split', atmosphere: 'paths' },
    prism: { title: 'You bring the idea. We bring clarity.', description: 'A quieter relationship with technology, shaped around the work people are here to do.', eyebrow: 'Intelligence, thoughtfully applied', align: 'center', atmosphere: 'ribs' },
    atelier: { title: 'Design with care. Create with purpose.', description: 'From a first thought to a useful experience. Precise details and a generous canvas for your next project.', eyebrow: 'An independent design practice', align: 'split', atmosphere: 'pixels' },
    landscape: { title: 'More space. A clearer view.', description: 'Useful product details, staged in open air. A considered system for the ideas you want to bring to life.', eyebrow: 'Made for everyday possibility', align: 'center' }
  };
  const recipe = $derived(recipes[direction]);
  const hasArt = $derived(!['meadow', 'equilibrium', 'prism', 'landscape', 'spectral'].includes(direction));
  const code = $derived(`<script lang="ts">\n  import '@tactile-ui/tokens/styles.css';\n  import { Theme, Surface, Button } from '@tactile-ui/svelte';\n<\/script>\n\n<Theme direction="${direction}">\n  <Surface><Button>Continue</Button></Surface>\n</Theme>`);
  const compositionCode = $derived(`<script lang="ts">\n  import '@tactile-ui/tokens/styles.css';\n  import { Theme, MarketingHero, MotionStage, ActionLink, MaterialObject } from '@tactile-ui/svelte';\n<\/script>\n\n<Theme direction="${direction}">\n  <MotionStage paused={false} intensity={0.6}>\n    <MarketingHero title="A little room for possibility." description="Your real product promise." align="split">\n      <ActionLink href="/start">Get started</ActionLink>\n      {#snippet art()}<div class="tui-stage-object"><MaterialObject kind="orb" /></div>{/snippet}\n    </MarketingHero>\n  </MotionStage>\n</Theme>`);
  async function chooseDirection(next: Direction) {
    direction = next;
    await tick();
    directionHeading?.scrollIntoView({ block: 'start', behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  }
  function createOutline(value: string) {
    if (value.length < 4) { taskError = 'Describe your idea in at least four characters.'; return; }
    taskError = '';
    outline = value;
    status = 'Your local demonstration outline is ready. You can edit the idea or reset it.';
  }
  async function copyCode(value: string) {
    try { await navigator.clipboard.writeText(value); status = 'Svelte snippet copied.'; }
    catch { status = 'Select and copy the snippet below.'; }
  }
  function saveName(event: SubmitEvent) {
    event.preventDefault();
    nameError = name.trim() ? '' : 'Enter a name for this demonstration workspace.';
    status = nameError ? 'Add a workspace name to continue.' : `“${name.trim()}” is saved for this page demonstration.`;
  }
</script>

<svelte:head><title>Tactile UI · Svelte reference gallery</title><meta name="description" content="Twelve distinct visual directions and reusable Svelte 5 components, inspired by 36 supplied reference images." /></svelte:head>

{#snippet heroArt()}
  {#if direction === 'porcelain'}
    <FileStack title="A place for your ideas" {files} />
  {:else if direction === 'editorial'}
    <div class="gallery-editorial-art"><Sparkline values={[2, 3, 5, 8, 13, 20, 30, 43]} label="Decorative sample curve: 2, 3, 5, 8, 13, 20, 30, 43." /><div class="gallery-editorial-note"><Orb appearance="accent">✳</Orb><span>One considered detail.</span></div></div>
  {:else if direction === 'citrus'}
    <div class="gallery-citrus-stage"><div class="gallery-orbit gallery-orbit-one tui-stage-object"><MaterialObject kind="coin" /></div><div class="gallery-orbit gallery-orbit-two tui-stage-object"><MaterialObject kind="coin" /></div><div class="gallery-orbit gallery-orbit-three tui-stage-object"><MaterialObject kind="coin" /></div><div class="gallery-citrus-devices"><DeviceFrame label="A demonstration project workspace" className="gallery-desktop-preview">{@render workspacePreview()}</DeviceFrame><DeviceFrame label="The same context, on the go" variant="phone" className="gallery-phone-preview"><div class="gallery-phone-ui"><p class="gallery-eyebrow">Your next idea</p><strong>Room for<br />possibility.</strong><MaterialObject kind="sun" /><span class="gallery-phone-divider"></span><p>3 clear next steps</p><Button variant="secondary" onclick={() => { dialogOpen = true; }}>Open preview</Button></div></DeviceFrame></div></div>
  {:else if direction === 'signal'}
    <Surface depth="flat"><table class="gallery-table"><caption>Illustrative project queue</caption><thead><tr><th scope="col">Project</th><th scope="col">Status</th></tr></thead><tbody><tr><td>Research notes</td><td><Badge tone="success">Reviewed</Badge></td></tr><tr><td>Source context</td><td><Badge tone="warning">Needs context</Badge></td></tr><tr><td>New ideas</td><td><Badge>Queued</Badge></td></tr></tbody></table></Surface>
  {:else if direction === 'connected' || direction === 'systems'}
    <IntegrationMap {nodes} title="Your working context" detail="An illustrative relationship map">
      {#snippet center()}<div class="tui-stage-object"><FrostedIcon /></div>{/snippet}
    </IntegrationMap>
  {:else if direction === 'atelier'}
    <div class="gallery-studio-notes"><div><span aria-hidden="true">⠿</span><strong>48 hours</strong><small>A sample project rhythm</small></div><div><span aria-hidden="true">⠿</span><strong>Thoughtful details</strong><small>From the first screen to the last</small></div></div>
  {/if}
{/snippet}

{#snippet workspacePreview()}
  <div class="gallery-product-ui"><aside class="gallery-product-sidebar"><strong>Tactile</strong><span class="gallery-product-nav-active">Overview</span><span>Projects</span><span>Notes</span><span>Activity</span><span class="gallery-product-sidebar-bottom">Your workspace</span></aside><div class="gallery-product-main"><div class="gallery-product-welcome"><div><p class="gallery-eyebrow">Your working context</p><h3>A little further, every day.</h3></div><AvatarStack items={people} max={3} /></div><SegmentedControl label="Preview view" value={previewMode} onValueChange={value => { previewMode = value; }} options={[{ value: 'overview', label: 'Overview' }, { value: 'progress', label: 'Progress' }]} />{#if previewMode === 'overview'}<div class="gallery-product-metrics"><div><span>Active projects</span><strong>12</strong><small>Demonstration workspace</small></div><div><span>Ideas collected</span><strong>36</strong><small>Ready to take shape</small></div></div><div class="gallery-product-chart"><p>Project activity</p><Sparkline values={[4, 8, 6, 12, 10, 14, 20, 18, 25]} label="Illustrative weekly activity counts: 4, 8, 6, 12, 10, 14, 20, 18, 25." /></div>{:else}<div class="gallery-product-progress"><Meter label="Research notes" value={8} max={12} valueText="8 of 12 sample notes" /><Meter label="Design exploration" value={4} max={8} valueText="4 of 8 sample studies" /><Meter label="Team context" value={6} max={10} valueText="6 of 10 sample updates" /></div>{/if}<div class="gallery-product-list"><span><strong>Research notes</strong><Badge tone="success">Ready</Badge></span><span><strong>New possibilities</strong><Badge tone="info">In progress</Badge></span><span><strong>Shared context</strong><Badge>Collected</Badge></span></div></div></div>
{/snippet}

{#snippet previewArt(kind: string)}
  <div class="gallery-landscape-preview"><AmbientBackdrop kind="landscape" /><DeviceFrame label="An illustrative product detail" variant={kind === 'progress' ? 'phone' : 'desktop'} className="gallery-preview-panel">
    {#if kind === 'files'}<p class="gallery-eyebrow">Your working context</p><strong class="gallery-preview-title">A place for every idea.</strong><div class="gallery-mini-files"><span>↗ Research</span><span>↗ New ideas</span><span>↗ Team notes</span></div><AvatarStack items={people} max={3} />
    {:else if kind === 'progress'}<p class="gallery-eyebrow">Sample project progress</p><strong class="gallery-preview-title">A little further, every day.</strong><Meter label="Illustrative progress" value={72} max={100} valueText="72 of 100 sample steps" />
    {:else}<p class="gallery-eyebrow">Illustrative activity</p><strong class="gallery-preview-title">See the work take shape.</strong><Sparkline values={[2, 6, 4, 10, 8, 12, 14]} label="Seven sample activity counts: 2, 6, 4, 10, 8, 12, 14." />{/if}
  </DeviceFrame></div>
{/snippet}

{#snippet anatomy()}
  <div class="kit-stack"><h3 class="tui-heading">Depth with a purpose.</h3><p class="kit-muted">One background plane, a crisp card edge, and a soft contact shadow. Reading surfaces stay calm.</p><div class="kit-grid-two"><Surface depth="recessed"><p class="kit-muted">Recessed plane</p></Surface><Surface depth="floating"><p class="kit-muted">Floating plane</p></Surface></div></div>
{/snippet}
{#snippet usage()}
  <div class="kit-stack"><pre class="kit-code"><code>{code}</code></pre><Button variant="secondary" onclick={() => copyCode(code)}>Copy Svelte snippet</Button></div>
{/snippet}
{#snippet behavior()}
  <div class="kit-stack"><h3 class="tui-heading">Built around real interaction.</h3><p class="kit-muted">Use Arrow keys, Home, and End between tabs. Escape closes the native dialog and returns focus to the trigger. Turn on reduced motion in your system settings to remove decorative movement.</p><Button variant="secondary" onclick={() => { dialogOpen = true; }}>Try the native dialog</Button></div>
{/snippet}
{#snippet startAnswer()}<p>Choose one visual direction, supply real content, and compose the components around a useful task. The packaged API works in Svelte 5 and React.</p>{/snippet}
{#snippet motionAnswer()}<p>Ambient motion can be paused at any time. MotionStage also stops when it is off screen or your system requests reduced motion. Actions and their outcomes remain available.</p>{/snippet}
{#snippet contentAnswer()}<p>These interfaces use demonstration content. Replace it with your own product state and keep loading, empty, failure, and success states visible.</p>{/snippet}

<Theme {direction} class="kit-page">
  <a href="#gallery-main" class="gallery-skip-link">Skip to the gallery</a>
  <header class="kit-header"><div class="kit-brand"><span class="kit-brand-mark" aria-hidden="true">↗</span>Tactile / UI <small>Reference kit · 02</small></div><div class="kit-row"><small>12 directions · 36 images</small><Button variant="ghost" onclick={() => { ambientMotion = !ambientMotion; }}>{ambientMotion ? 'Pause motion' : 'Resume motion'}</Button><Badge>Svelte 5</Badge></div></header>
  <div class="kit-mobile-direction-picker"><label for={directionSelectId}>Design direction</label><select id={directionSelectId} aria-label="Design direction" value={direction} onchange={event => chooseDirection(event.currentTarget.value as Direction)}>{#each directions as item (item.id)}<option value={item.id}>{item.name}</option>{/each}</select></div>
  <div class="kit-workspace">
    <nav class="kit-nav" aria-label="Design directions"><p class="kit-eyebrow">Choose a direction</p>
      {#each directions as item, index (item.id)}<button type="button" aria-pressed={direction === item.id} onclick={() => chooseDirection(item.id)}><span>{String(index + 1).padStart(2, '0')}</span>{item.name}</button>{/each}
      <p class="kit-nav-note">A study of 36 supplied images.<br />Twelve distinct compositions.<br />A shared component language.</p>
    </nav>
    <main class="kit-main" id="gallery-main">
      <div class="kit-title-row gallery-direction-heading" bind:this={directionHeading}><div><p class="gallery-page-title">{preset.name}</p><p>{preset.note}</p></div><span class="kit-ref">References {preset.refs}</span></div>
      <section class="gallery-recipe" data-recipe={direction} aria-label={`${preset.name} composition`}>
        <MotionStage paused={!ambientMotion} intensity={0.6} className="gallery-stage">
        {#if recipe.atmosphere}<AmbientBackdrop kind={recipe.atmosphere} animated={ambientMotion} />{/if}
        <SiteHeader brand={direction === 'atelier' ? '✳ Studio' : 'Tactile'} homeHref="#gallery-main" items={[{ label: 'Components', href: '#components' }, { label: 'Ingredients', href: '#ingredients' }, { label: 'Use the kit', href: '#setup' }]} action={{ label: 'Explore the kit', href: '#components' }} />
        <MarketingHero eyebrow={recipe.eyebrow} title={recipe.title} description={recipe.description} align={recipe.align} art={hasArt ? heroArt : undefined}>
          {#if direction === 'meadow'}<TaskComposer label="What would you like to create?" value={task} onValueChange={value => { task = value; taskError = ''; }} onSubmit={createOutline} error={taskError} submitLabel="Create outline" placeholder="Plan a weekend in Lisbon" hint="An interactive local demonstration. Your idea stays on this page." />
          {:else}
          <ActionLink href="#components">{direction === 'atelier' ? 'View the details' : 'Explore the components'} ↗</ActionLink>
          <ActionLink href="#setup" variant="secondary">Use in your project</ActionLink>
          {/if}
        </MarketingHero>
        {#if direction === 'meadow'}<div class="gallery-start-options"><ActionLink href="#ingredients" variant="secondary"><span class="gallery-import-icon" aria-hidden="true">N</span>Start with notes</ActionLink><ActionLink href="#ingredients" variant="secondary"><span class="gallery-import-icon" aria-hidden="true">▥</span>Start with files</ActionLink><ActionLink href="#setup" variant="secondary"><span class="gallery-import-icon" aria-hidden="true">↗</span>Start from the kit</ActionLink></div>{#if outline}<div class="gallery-outline" aria-live="polite"><div class="gallery-outline-head"><div><p class="gallery-eyebrow">Your local outline</p><h2>{outline}</h2></div><Button variant="ghost" onclick={() => { outline = ''; status = 'Outline reset. Your original idea is still available to edit.'; }}>Reset outline</Button></div><ol><li><span>01</span><div><strong>Collect the useful details</strong><p>Gather your notes, preferences, and places to explore.</p></div></li><li><span>02</span><div><strong>Give the idea a little structure</strong><p>Choose a starting point and the next steps that matter to you.</p></div></li><li><span>03</span><div><strong>Make room for possibility</strong><p>Review the outline, edit your idea, and shape what happens next.</p></div></li></ol></div>{/if}<p class="gallery-meadow-footnote">A little room to begin.</p>
        {:else if direction === 'equilibrium'}<div class="gallery-equilibrium-content"><SectionHeading title="A considered structure for complex work." align="center" /><div class="gallery-triptych"><ProcessCard title="Gather" description="Bring useful context together, with the source and purpose of every piece still visible." step="01" mark="scatter" /><ProcessCard title="Shape" description="Give ideas a clear structure. Keep the information readable and the relationships precise." step="02" mark="align" /><ProcessCard title="Move" description="Turn a clear view of the work into a useful next step. Each action has a visible outcome." step="03" mark="transfer" /></div></div>
        {:else if direction === 'prism'}<div class="gallery-manifesto"><p class="gallery-eyebrow">A more thoughtful relationship</p><p class="gallery-manifesto-copy">Technology should give people room to think. Clear tools, considered details, and a steady rhythm help the work feel human.</p><div class="gallery-manifesto-bottom"><div class="tui-stage-object"><MaterialObject kind="sun" /></div><span>Useful by design.<br />Thoughtful in every detail.</span></div></div>
        {:else if direction === 'spectral'}<div class="gallery-triptych gallery-poster-row"><PosterCard title="Make room for possibility." description="A calm canvas with a vivid focal point." palette="blue" /><PosterCard title="Build with a lighter touch." description="Soft light. Confident, readable type." palette="violet" /><PosterCard title="Bring your tools together." description="One visual system, many useful components." palette="ice" /></div>
        {:else if direction === 'landscape'}<div class="gallery-triptych gallery-landscape-row"><ShowcaseCard title="A home for ideas" description="Bring your notes and source material into a clear working context." tone="meadow">{#snippet art()}{@render previewArt('files')}{/snippet}</ShowcaseCard><ShowcaseCard title="A visible next step" description="Show what has happened and what still needs your attention." tone="blue">{#snippet art()}{@render previewArt('progress')}{/snippet}</ShowcaseCard><ShowcaseCard title="A clearer view" description="Turn sample activity into a readable, explicitly labeled picture." tone="lavender">{#snippet art()}{@render previewArt('activity')}{/snippet}</ShowcaseCard></div>
        {/if}
        </MotionStage>
      </section>

      <div class="gallery-section" id="components"><SectionHeading eyebrow="The component language" title="The details that make it feel considered." description="Working native controls. Readable surfaces. Visible states." /></div>
      <div class="kit-specimens">
        <Surface class="kit-controls"><div class="kit-stack"><div class="kit-row"><Button onclick={() => { dialogOpen = true; }}>Primary action ↗</Button><Button variant="secondary" onclick={() => { status = 'Secondary action selected in this demonstration.'; }}>Secondary</Button><Button variant="ghost" disabled>Disabled</Button><Button loading>Saving</Button></div><div class="kit-row"><Badge tone="success">Ready</Badge><Badge tone="warning">Needs attention</Badge><Badge tone="danger">Action failed</Badge><Badge tone="info">Sample data</Badge></div><form class="kit-stack" onsubmit={saveName}><Field label="Workspace name" bind:value={name} error={nameError} hint="A visible label and linked help text." placeholder="Your next idea" /><div class="kit-row"><Button type="submit" variant="secondary">Save demo name</Button><Switch bind:checked={texture} label="Decorative texture" /><Switch bind:checked={ambientMotion} label="Ambient motion" /></div></form><p class="kit-status" aria-live="polite">{status}</p></div></Surface>
        <MetricCard label="Sample project files" value="128" detail="A string display value, supplied by the app." note="Illustrative data; the chart is a visual, not a financial calculation."><Sparkline values={[12, 28, 22, 35, 48, 62, 70, 68, 93, 110, 128]} label="Eleven sample counts: 12, 28, 22, 35, 48, 62, 70, 68, 93, 110, 128." /><Meter label="Illustrative progress" value={128} max={200} valueText="128 of 200 sample files" /></MetricCard>
        <FeatureCard title="Connect with confidence." description="A raised frame, a central object, and quiet supporting detail.">{#snippet art()}<Shield />{/snippet}</FeatureCard>
        <Surface class="kit-controls"><Tabs label="Component details" bind:value={tab} items={[{ id: 'anatomy', label: 'Anatomy', content: anatomy }, { id: 'usage', label: 'Use in your project', content: usage }, { id: 'behavior', label: 'Keyboard & motion', content: behavior }]} /></Surface>
        <Surface class="kit-wide" texture={texture ? 'dots' : 'none'}><IntegrationMap title="Thoughtful connections" detail="Labels stay readable as the layout stacks on small screens." {nodes} /></Surface>
        <OnboardingCard title="Welcome to your next idea." description="Pastel atmosphere above; a plain, readable action area below." {step} steps={4} onContinue={() => { step = step === 4 ? 1 : step + 1; }} continueLabel={step === 4 ? 'Restart demo' : 'Continue'}>{#snippet art()}<Orb appearance="iridescent">☼</Orb>{/snippet}</OnboardingCard>
        <Surface class="kit-controls" id="setup"><div class="kit-stack"><h3 class="tui-heading">Build from the ingredients.</h3><p class="kit-muted">Choose a direction, supply real product content, and compose around the task. These are reusable Svelte components.</p><pre class="kit-code"><code>{compositionCode}</code></pre><div class="kit-row"><Button variant="secondary" onclick={() => copyCode(compositionCode)}>Copy composition</Button><Badge>React + Svelte parity</Badge></div></div></Surface>
        <Surface class="kit-controls"><div class="kit-stack"><h3 class="tui-heading">A clear view, in every state.</h3><SegmentedControl label="Project filter" value={fileFilter} onValueChange={value => { fileFilter = value; }} options={[{ value: 'all', label: 'All projects' }, { value: 'favorites', label: 'Favorites' }, { value: 'archived', label: 'Archived', disabled: true }]} />{#if fileFilter === 'all'}<FileStack title="Your project files" {files} />{:else}<EmptyState title="No favorites yet." description="Keep your most useful projects close. Choose All projects to find the next one."><Button variant="secondary" onclick={() => { fileFilter = 'all'; }}>Show all projects</Button>{#snippet art()}<FrostedIcon />{/snippet}</EmptyState>{/if}</div></Surface>
        <Surface class="kit-controls"><div class="kit-stack"><h3 class="tui-heading">Thoughtful feedback.</h3><InlineNotice title="A little context goes a long way." tone="info"><p>Give people a readable state and a useful next action. Keep every outcome visible without relying on color.</p></InlineNotice><div class="kit-row"><AvatarStack items={people} max={3} /><span class="kit-muted">A shared place to think.</span></div><Button variant="secondary" onclick={() => { loadingPreview = !loadingPreview; }}>{loadingPreview ? 'Show loaded preview' : 'Show loading preview'}</Button>{#if loadingPreview}<p role="status" class="kit-muted">Loading preview demonstration…</p><Skeleton lines={3} />{:else}<p class="kit-muted">The preview is ready. This toggle demonstrates the loading visual locally.</p>{/if}</div></Surface>
        <Surface class="kit-wide"><Accordion label="Using the kit" items={[{ id: 'start', title: 'How do I begin?', content: startAnswer }, { id: 'motion', title: 'How does motion respond to preferences?', content: motionAnswer }, { id: 'content', title: 'What should I put in the components?', content: contentAnswer }]} /></Surface>
      </div>

      <section class="gallery-section" id="ingredients" aria-label="Texture and illustration ingredients"><SectionHeading eyebrow="A shared visual vocabulary" title="Light, texture, and a useful focal point." description="Decoration belongs around the task. Labels and actions remain clear." /><div class="gallery-ingredients"><Surface texture={texture ? 'grain' : 'none'}><FrostedIcon /><h3 class="tui-heading">Frosted layers</h3><p class="tui-caption">A decorative icon with a readable card beside it.</p></Surface><Surface texture={texture ? 'lines' : 'none'}><FileStack title="A little structure" {files} /></Surface><Surface texture={texture ? 'dots' : 'none'}><div class="gallery-orb-row"><Orb appearance="neutral">✳</Orb><Orb appearance="accent">↗</Orb><Orb appearance="iridescent">☼</Orb></div><h3 class="tui-heading">A physical detail</h3><p class="tui-caption">One contact shadow. A restrained highlight.</p></Surface></div><div class="gallery-atmosphere-grid">{#each ['meadow', 'contours', 'paths', 'ribs', 'pixels', 'scanlines', 'landscape'] as kind}<div class="gallery-atmosphere-swatch"><AmbientBackdrop kind={kind as Atmosphere} animated={ambientMotion} /><span>{kind}</span></div>{/each}</div></section>
      <Reveal><Surface class="gallery-motion-note"><SectionHeading title="A quiet entrance. A visible result." description="This below-the-fold panel reveals once on entry. Server-rendered content stays visible without JavaScript; reduced motion shows it immediately." /><ActionLink href="#gallery-main" variant="secondary">Back to the direction</ActionLink></Surface></Reveal>
      <section class="gallery-section" aria-label="Material object library"><SectionHeading eyebrow="A grounded focal point" title="Light, material, and a coherent shape." description="Four reusable sculptures. One consistent material language." /><MotionStage paused={!ambientMotion} intensity={0.4} className="gallery-material-shelf">{#each ['orb', 'coin', 'sun', 'certificate'] as kind}<div class="gallery-material-specimen"><div class="tui-stage-object"><MaterialObject kind={kind as 'orb' | 'coin' | 'sun' | 'certificate'} /></div><span>{kind}</span></div>{/each}</MotionStage></section>
      <footer class="kit-footer"><span>Original components inspired by 36 supplied reference images.</span><span>All content and counts are demonstration fixtures.</span></footer>
    </main>
  </div>
  <Dialog bind:open={dialogOpen} title="A little room for focus."><div class="gallery-dialog-art"><Orb appearance="accent">✳</Orb></div><p class="kit-dialog-copy">A native modal with a quiet backdrop, a visible close control, and focus returned to the trigger.</p><Button onclick={() => { dialogOpen = false; status = 'Demo dialog completed.'; }}>Continue exploring</Button></Dialog>
</Theme>
