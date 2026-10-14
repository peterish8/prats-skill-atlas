<script lang="ts">
  import '@tactile-ui/tokens/styles.css';
  import './recipe.css';
  import { Accordion, AmbientBackdrop, Badge, Button, DeviceFrame, EmptyState, FileStack,
    InlineNotice, MarketingHero, MotionStage, ProcessCard, SectionHeading, SiteHeader,
    TaskComposer, Theme } from '@tactile-ui/svelte';
  let value = $state('');
  let outline = $state('');
  let paused = $state(false);
  let error = $state<string>();
  function createOutline(task: string) {
    if (task.length > 160) { error = 'Keep this outline title to 160 characters.'; return; }
    error = undefined;
    outline = task;
  }
</script>

<Theme direction="meadow" class="reference-page">
  <MotionStage {paused} intensity={.35}>
    <div class="reference-hero" id="top">
      <AmbientBackdrop kind="meadow" animated={!paused}/>
      <SiteHeader brand="Commonplace" homeHref="#top"
        items={[{label:'How it works',href:'#process'},{label:'Your outline',href:'#preview'},{label:'Help',href:'#help'}]}
        action={{label:'Try it',href:'#compose'}}/>
      <MarketingHero title="Give your next idea a place."
        description="Start with a short description. Shape a first outline, then decide what comes next.">
        <div id="compose"><TaskComposer label="What would you like to make?" {value}
          onValueChange={next => { value=next; error=undefined; }} onSubmit={createOutline}
          submitLabel="Create outline" placeholder="A field guide for weekend walks" maxLength={160}
          hint="This local preview is not saved; reloading clears it." {error}/></div>
      </MarketingHero>
      <div class="reference-toolbar"><Button variant="ghost" aria-pressed={paused}
        onclick={() => paused=!paused}>{paused ? 'Resume atmosphere' : 'Pause atmosphere'}</Button></div>
    </div>
    <main>
      <section class="reference-content" id="preview">
        <SectionHeading eyebrow="Your starting point" title="An idea, made tangible."
          description="The outline keeps three useful next steps together." align="center"/>
        <div class="reference-result" role="status" aria-live="polite">
          {#if outline}
            <InlineNotice title="Your local outline is ready" tone="success">{outline}</InlineNotice>
            <div style="margin-top:24px" class="tui-stage-object">
              <DeviceFrame label="Local outline preview; not saved" variant="desktop">
                <Badge tone="info">Editable starting point</Badge>
                <FileStack title={outline} files={[
                  {id:'question',name:'The question',detail:'Write what you want to discover',kind:'document'},
                  {id:'materials',name:'Materials',detail:'Gather the useful pieces',kind:'folder'},
                  {id:'next',name:'Next step',detail:'Choose one small action',kind:'document'}]}/>
              </DeviceFrame>
            </div>
            <div class="reference-toolbar" style="margin-top:24px"><Button variant="secondary"
              onclick={() => {outline='';value='';}}>Start another</Button></div>
          {:else}
            <EmptyState title="Your idea starts here" description="Describe an idea above to create its first local outline."/>
          {/if}
        </div>
      </section>
      <section class="reference-content" id="process">
        <SectionHeading eyebrow="A simple rhythm" title="From a thought to a next step." align="center"/>
        <div class="reference-grid">
          <ProcessCard title="Collect" description="Name the question and gather the things that matter." step="01" mark="scatter"/>
          <ProcessCard title="Shape" description="Put related pieces beside each other and give them a clear place." step="02" mark="align"/>
          <ProcessCard title="Continue" description="Choose a useful next action and return when the idea grows." step="03" mark="transfer"/>
        </div>
      </section>
      <section class="reference-content" id="help">
        <SectionHeading title="A few useful details."/>
        {#snippet savedHelp()}<p>This demonstration stores the title in page memory. Reloading clears it. A product should connect its own saved-project flow.</p>{/snippet}
        {#snippet motionHelp()}<p>Use Pause atmosphere above. Your system reduced-motion preference also removes nonessential movement.</p>{/snippet}
        <Accordion label="Outline help" items={[
          {id:'saved',title:'Is this outline saved?',content:savedHelp},
          {id:'motion',title:'Can I stop the movement?',content:motionHelp}]}/>
      </section>
    </main>
    <footer class="reference-footer">A small space to begin. Local demonstration.</footer>
  </MotionStage>
</Theme>
