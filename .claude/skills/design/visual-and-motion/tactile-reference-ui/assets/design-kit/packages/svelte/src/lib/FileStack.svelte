<script lang="ts">
 import { cx,type FileItem } from '@tactile-ui/tokens';
 interface Props {title:string;files:FileItem[];class?:string}
 let {title,files,class:className}:Props=$props();
</script>
<section class={cx('tui-file-stack',className)} aria-label={title}><h3 class="tui-heading">{title}</h3><ul class="tui-file-list">{#each files as file (file.id)}<li class="tui-file" data-kind={file.kind || 'folder'}><div class="tui-file-icon" aria-hidden="true"></div><strong>{file.name}</strong><small>{file.detail}</small></li>{/each}</ul></section>
