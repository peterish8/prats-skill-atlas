import { useState } from 'react';
import {
  ActionLink, AmbientBackdrop, Badge, Field, FileStack, FrostedIcon,
  IntegrationMap, MarketingHero, Meter, Reveal, SectionHeading,
  ShowcaseCard, SiteHeader, Sparkline, Surface, MotionStage, TaskComposer,
  ProcessCard, DeviceFrame, MaterialObject, Button, Accordion, SegmentedControl,
  InlineNotice, EmptyState, AvatarStack, Skeleton
} from '@tactile-ui/react';
import type { Direction } from '@tactile-ui/tokens';

const navigation = [
  { label: 'Components', href: '#component-language' },
  { label: 'How to use', href: '#implementation' },
  { label: 'Design notes', href: '#recipe-notes' }
];

const connections = [
  { id: 'source', label: 'Source files', detail: 'Inputs in their own context', symbol: 'S' },
  { id: 'notes', label: 'Team notes', detail: 'A shared point of view', symbol: 'N' },
  { id: 'review', label: 'Review', detail: 'A deliberate human step', symbol: 'R' },
  { id: 'output', label: 'Output', detail: 'Ready for your next task', symbol: 'O' }
];

function RecipeHeader({ brand }: { brand: string }) {
  return <SiteHeader brand={brand} homeHref="#gallery-top" items={navigation} action={{ label: 'Explore the kit', href: '#component-language' }}/>;
}

function RecipeActions({ primary = 'Explore the components' }: { primary?: string }) {
  return <><ActionLink href="#component-language">{primary} <span aria-hidden="true">↗</span></ActionLink><ActionLink href="#implementation" variant="secondary">Build with this direction</ActionLink></>;
}

/** These are original, semantic product previews, not flattened reference screenshots. */
function NotesPreview() {
  return <div className="rx-product-preview rx-notes-preview"><div className="rx-preview-top"><span className="rx-preview-symbol" aria-hidden="true">✳</span><strong>Field notes</strong><Badge tone="success">Saved</Badge></div>
    <p className="rx-preview-label">Selected collection</p><h4>A little room to think.</h4>
    <ul><li><span aria-hidden="true">▤</span> Patterns in the everyday <small>Note</small></li><li><span aria-hidden="true">▤</span> A new point of view <small>Note</small></li><li><span aria-hidden="true">▤</span> Things to come back to <small>Note</small></li></ul>
  </div>;
}

function CollectionPreview() {
  return <div className="rx-product-preview rx-collection-preview"><div className="rx-preview-top"><strong>Reading collection</strong><Badge>3 sample notes</Badge></div>
    <table><caption>Ideas worth returning to</caption><thead><tr><th scope="col">Title</th><th scope="col">Type</th></tr></thead><tbody><tr><td>The shape of a day</td><td>Essay</td></tr><tr><td>A better question</td><td>Note</td></tr><tr><td>Space for ideas</td><td>Guide</td></tr></tbody></table>
  </div>;
}

function ProgressPreview() {
  return <div className="rx-product-preview rx-progress-preview"><div className="rx-preview-top"><strong>Project overview</strong><Badge tone="info">Demo</Badge></div>
    <div className="rx-preview-metric"><strong>12</strong><span>Sample files organized</span></div>
    <Sparkline values={[2, 4, 3, 6, 8, 9, 12]} label="Illustrative organized file counts: 2, 4, 3, 6, 8, 9, 12."/>
    <Meter label="Sample review progress" value={3} max={4} valueText="3 of 4 tasks"/>
  </div>;
}

export function MarketingRecipe({ direction, texture, animated }: { direction: Direction; texture: boolean; animated: boolean }) {
  return <MotionStage paused={!animated} intensity={.6} className="rx-scene"><RecipeScene direction={direction} texture={texture} animated={animated}/></MotionStage>;
}

function RecipeScene({ direction, texture, animated }: { direction: Direction; texture: boolean; animated: boolean }) {
  const [task, setTask] = useState('Plan a thoughtful weekend in Kyoto');
  const [outline, setOutline] = useState('');
  const [screen, setScreen] = useState('notes');
  const starters = [
    { title: 'Research project', detail: 'A clear place to begin', value: 'Organize a new research project', symbol: '▤' },
    { title: 'Weekend itinerary', detail: 'A little room to explore', value: 'Plan a thoughtful weekend in Kyoto', symbol: '⌁' },
    { title: 'Reading collection', detail: 'Gather your next ideas', value: 'Build a reading collection for the month', symbol: '▦' }
  ];
  if (direction === 'meadow') return <div className="rx-recipe rx-meadow">
    {texture && <AmbientBackdrop kind="meadow" animated={animated}/>}
    <RecipeHeader brand="field / notes"/>
    <MarketingHero eyebrow="A gentler way to get there" title="Make room for your next idea." description="Gather what matters. Give it a little structure. Find your own way forward.">
      <TaskComposer label="What would you like to organize?" value={task} onValueChange={setTask} onSubmit={setOutline} submitLabel="Make an outline" placeholder="Describe your next idea" hint="A local, editable outline demo. No provider request is made."/>
    </MarketingHero>
    <div className="rx-starter-row">{starters.map(starter => <button key={starter.title} type="button" aria-pressed={task === starter.value} onClick={() => { setTask(starter.value); setOutline(''); }}><span aria-hidden="true">{starter.symbol}</span><strong>{starter.title}</strong><small>{starter.detail}</small></button>)}</div>
    {outline && <div className="rx-outline-result" data-complete="true"><InlineNotice title="Your outline is ready" tone="success"><strong>{outline}</strong><ol><li>Gather the useful notes and starting points.</li><li>Group the details into a few clear themes.</li><li>Choose the first small step.</li></ol><Button variant="ghost" onClick={() => setOutline('')}>Clear this outline</Button></InlineNotice></div>}
    <p className="rx-quiet-caption" role="status">{outline ? 'Outline created. Edit the prompt to make another.' : 'A quieter canvas. A clearer invitation.'}</p>
  </div>;

  if (direction === 'equilibrium') return <div className="rx-recipe rx-equilibrium">
    {texture && <AmbientBackdrop kind="contours" animated={animated}/>}
    <RecipeHeader brand="equilibrium"/>
    <MarketingHero eyebrow="Structure for what comes next" title="Where complexity finds its balance." description="Start with the important parts. Connect them with care. Move forward with a clearer view."><RecipeActions primary="See the structure"/></MarketingHero>
    <div className="rx-axis" aria-hidden="true"/>
    <SectionHeading title="A little structure changes everything." align="center" description="Three deliberate steps, with room to understand each one."/>
    <div className="rx-process-grid"><Reveal><ProcessCard mark="scatter" step="01 / Understand" title="Find the pieces." description="Keep the original context. Identify what belongs together before making a connection."/></Reveal><Reveal delay={70}><ProcessCard mark="align" step="02 / Arrange" title="Give them a place." description="Use consistent labels and a clear hierarchy so every detail can be found again."/></Reveal><Reveal delay={140}><ProcessCard mark="transfer" step="03 / Continue" title="Make the next move." description="Present a useful next step with its purpose and supporting context intact."/></Reveal></div>
  </div>;

  if (direction === 'systems') return <div className="rx-recipe rx-systems">
    {texture && <AmbientBackdrop kind="paths" animated={animated}/>}
    <RecipeHeader brand="common / ground"/>
    <MarketingHero align="split" eyebrow="Connected, with intention" title="The infrastructure behind a clearer day." description="A shared place for source material, team context, and the decisions that connect them." art={<div className="rx-system-art"><IntegrationMap nodes={connections} title="Your workspace" detail="A visible relationship between useful things" center={<MaterialObject kind="orb" className="tui-stage-object rx-system-object"/>}/></div>}><RecipeActions primary="Follow the connections"/></MarketingHero>
    <div className="rx-system-strip"><span><strong>Inputs</strong> Keep their context</span><span><strong>Decisions</strong> Have a visible owner</span><span><strong>Outputs</strong> Lead somewhere useful</span></div>
  </div>;

  if (direction === 'prism') return <div className="rx-recipe rx-prism">
    <div className="rx-prism-stage">{texture && <AmbientBackdrop kind="ribs" animated={animated}/>}
      <RecipeHeader brand="prism."/>
      <MarketingHero eyebrow="A clearer point of view" title="You bring the idea. We make room for it." description="Purposeful tools with enough space to help you see what comes next."><RecipeActions primary="Discover the ingredients"/></MarketingHero>
      <div className="rx-prism-object"><MaterialObject kind="sun" className="tui-stage-object"/></div>
    </div>
    <Reveal className="rx-manifesto"><span className="rx-manifesto-label">Clarity, multiplied</span><div><SectionHeading title="Thoughtful interfaces leave room for people." description="Start with the task. Make its context visible. Keep the important choices close, and let everything else fall quietly into place."/><ActionLink href="#recipe-notes" variant="ghost">Read the design notes <span aria-hidden="true">↗</span></ActionLink></div></Reveal>
    <section className="rx-prism-product"><SectionHeading eyebrow="A considered set of tools" title="A little help, at every step." align="center"/><div className="rx-prism-orbit"><div><h3>Keep the full picture</h3><p>Context stays beside the content.</p></div><MaterialObject kind="orb" className="tui-stage-object"/><div><h3>Find the useful next step</h3><p>Stable controls. Clear consequences.</p></div></div></section>
  </div>;

  if (direction === 'atelier') return <div className="rx-recipe rx-atelier">
    {texture && <AmbientBackdrop kind="pixels" animated={animated}/>}
    <RecipeHeader brand="atelier / 01"/>
    <MarketingHero align="split" eyebrow="Independent ideas, carefully made" title="Design with intention. Create a little possibility." description="A crisp canvas, one graphic idea, and a simple path to the work." art={<div className="rx-studio-art"><div className="rx-studio-detail"><span className="rx-studio-mark" aria-hidden="true">▦</span><strong>Clear composition</strong><span>One point of focus</span></div><div className="rx-studio-detail"><span className="rx-studio-mark" aria-hidden="true">✳</span><strong>Useful detail</strong><span>Every interaction considered</span></div></div>}><RecipeActions primary="See the component study"/></MarketingHero>
    <Reveal className="rx-atelier-footer"><p>Explore the ingredients,<br/><strong>then make them your own.</strong></p><FrostedIcon/></Reveal>
  </div>;

  if (direction === 'landscape') return <div className="rx-recipe rx-landscape">
    <RecipeHeader brand="open / space"/>
    <MarketingHero eyebrow="Structure that adapts to you" title="More room for the work that matters." description="A simple way to gather ideas, organize the details, and see where you are."><RecipeActions primary="Explore the product details"/></MarketingHero>
    <div className="rx-landscape-grid"><Reveal><ShowcaseCard title="A place for your thoughts" description="Readable notes, a clear collection, and enough breathing room to find the useful detail." tone="meadow" art={<><AmbientBackdrop kind="landscape"/><NotesPreview/></>}/></Reveal><Reveal delay={70}><ShowcaseCard className="rx-landscape-center" title="A clearer view of progress" description="Small, honest summaries put the next task close to the information you need." tone="blue" art={<><AmbientBackdrop kind="landscape"/><ProgressPreview/></>}/></Reveal><Reveal delay={140}><ShowcaseCard title="Ideas worth returning to" description="A familiar table keeps the real content readable, even in a more expressive composition." tone="mint" art={<><AmbientBackdrop kind="landscape"/><CollectionPreview/></>}/></Reveal></div>
    <p className="rx-quiet-caption">Original product previews · all content is illustrative.</p>
  </div>;

  if (direction === 'citrus') return <div className="rx-recipe rx-citrus-product">
    {texture && <AmbientBackdrop kind="meadow" animated={animated}/>}
    <RecipeHeader brand="citrus / work"/>
    <MarketingHero eyebrow="A fresh place for useful things" title="Everything in the right place." description="A clear workspace for the ideas, notes, and projects that shape your day."><RecipeActions primary="Explore the workspace ingredients"/></MarketingHero>
    <div className="rx-citrus-pose"><MaterialObject kind="coin" className="tui-stage-object rx-citrus-coin-one"/><MaterialObject kind="coin" className="tui-stage-object rx-citrus-coin-two"/>
      <DeviceFrame variant="desktop" label="Original desktop workspace preview" className="rx-desktop-preview"><div className="rx-device-workspace"><aside><strong>citrus / work</strong><p>Ideas</p><p>Collections</p><p>Shared notes</p></aside><div><SegmentedControl label="Preview screen" value={screen} options={[{ value: 'notes', label: 'Notes' }, { value: 'collection', label: 'Collection' }]} onValueChange={setScreen}/>{screen === 'notes' ? <NotesPreview/> : <CollectionPreview/>}</div></div></DeviceFrame>
      <DeviceFrame variant="phone" label="Original phone workspace preview" className="rx-phone-preview"><div className="rx-phone-screen"><strong>citrus / work</strong>{screen === 'notes' ? <NotesPreview/> : <CollectionPreview/>}</div></DeviceFrame>
    </div><p className="rx-quiet-caption">Choose a preview screen. Both devices update together.</p>
  </div>;
  return null;
}

export function MarketingSpecimens() {
  const [view, setView] = useState('notes');
  const [value, setValue] = useState('Create a collection for my next project');
  const [result, setResult] = useState('');
  const [showLoading, setShowLoading] = useState(false);
  return <>
    <Surface className="kit-wide rx-marketing-specimens"><SectionHeading eyebrow="Page ingredients" title="Compose a useful first impression." description="Semantic navigation, a focused heading, original atmosphere, and readable product details."/>
      <div className="rx-specimen-links"><ActionLink href="#implementation">Open the setup example</ActionLink><ActionLink variant="secondary" href="#recipe-notes">Read the direction notes</ActionLink><ActionLink variant="ghost" href="#gallery-top">Back to the top <span aria-hidden="true">↑</span></ActionLink></div>
      <div className="rx-detail-grid"><div><FrostedIcon/><h3>One physical detail</h3><p className="kit-muted">Frosted layers belong in decorative art. Keep controls and reading surfaces crisp.</p></div><div><Field label="A visible example label" placeholder="A place for your next idea" hint="Connect this field to your own product behavior."/><p className="kit-muted">The visible label, focus treatment, and plain content area stay intact in every direction.</p></div></div>
    </Surface>
    <div className="kit-wide rx-triptych"><ShowcaseCard title="Spaces" description="Give each kind of work a familiar place." tone="lavender" art={<FileStack title="Sample spaces" files={[{ id: 'personal', name: 'Personal', detail: 'Ideas and notes' }, { id: 'team', name: 'Team', detail: 'Shared context' }]}/>}/><ShowcaseCard title="Folders & tags" description="Structure that helps you find your way back." tone="blue" art={<FileStack title="A clear hierarchy" files={[{ id: 'research', name: 'Research', detail: 'Source notes' }, { id: 'ideas', name: 'Ideas', detail: 'Things to explore' }]}/>}/><ShowcaseCard title="Collections" description="The content stays readable and useful." tone="mint" art={<CollectionPreview/>}/></div>
    <Surface className="kit-wide rx-functional-specimens"><SectionHeading eyebrow="Working state ingredients" title="The details keep their meaning." description="These controls change visible local state. Your application owns requests, loading, and persisted data."/><div className="rx-functional-grid"><div><SegmentedControl label="Show a specimen" value={view} onValueChange={setView} options={[{ value: 'notes', label: 'Notes' }, { value: 'collection', label: 'Collection' }, { value: 'empty', label: 'Empty state' }]}/>{view === 'notes' ? <NotesPreview/> : view === 'collection' ? <CollectionPreview/> : <EmptyState title="A little room for something new." description="Create a collection to give the next idea a place." art={<MaterialObject kind="certificate"/>}><Button onClick={() => { setView('collection'); setResult('A sample collection is ready below.'); }}>Create a sample collection</Button></EmptyState>}<AvatarStack items={[{ id: '1', name: 'Asha Rao, sample collaborator', initials: 'AR' }, { id: '2', name: 'Noah Kim, sample collaborator', initials: 'NK' }, { id: '3', name: 'Lena Cho, sample collaborator', initials: 'LC' }, { id: '4', name: 'Omar Lee, sample collaborator', initials: 'OL' }, { id: '5', name: 'Mina Chen, sample collaborator', initials: 'MC' }]}/><p className="kit-muted">Illustrative collaborator initials, with accessible full names.</p></div>
      <div><TaskComposer label="Try the reusable composer" value={value} onValueChange={setValue} onSubmit={intent => { setResult('Outline created for: ' + intent); setShowLoading(false); }} submitLabel="Create outline" hint="This demo records your typed intent immediately in local state." loading={showLoading}/>{result && <InlineNotice title="Local result" tone="success"><p role="status">{result}</p></InlineNotice>}<div className="rx-loading-demo"><Button variant="secondary" onClick={() => setShowLoading(!showLoading)}>{showLoading ? 'Finish loading demonstration' : 'Show loading state'}</Button>{showLoading && <div><p className="kit-muted" role="status">Loading state demonstration. Use the button above to finish it.</p><Skeleton lines={3}/></div>}</div></div></div>
      <Accordion label="Component behavior" items={[{ id: 'state', title: 'Where does the real data live?', content: <p>Your application owns values, requests, permissions, and persistence. TaskComposer and SegmentedControl receive values and report changes through callbacks.</p> }, { id: 'motion', title: 'What happens when motion is paused?', content: <p>Ambient movement stops. Inputs, selections, outline creation, native navigation, and details remain usable. System reduced motion removes physical travel independently.</p> }, { id: 'installation', title: 'How does this fit another app?', content: <p>Install the framework package and tokens, import the shipped stylesheet once, choose a Theme direction, and compose the public components. The React source has one component per file under controls, display, layout, and motion.</p> }]}/>
    </Surface>
  </>;
}
