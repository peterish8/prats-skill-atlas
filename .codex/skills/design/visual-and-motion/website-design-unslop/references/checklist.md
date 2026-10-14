# 150 website design and usability checks

Use these as inspection prompts for a specific product and brief. Visual patterns cannot establish who or what authored a site. Keep deliberate texture, 3D, gradients, shadows, and familiar patterns when they serve the approved direction.

Checks 1–100 adapt the user-provided starting list; 101–150 extend it. This revision clarifies broad rules and replaces repeated additions with distinct mechanisms. Exact applicability, inspection methods, basis, and source links are in audit-map.json and sources.md. The 2026-10-12 wording review is in checklist-review.md.

A heuristic needs product-specific justification. A standard needs its stated scope and exceptions. For a full audit use PASS, FAIL, NOT_APPLICABLE, or UNVERIFIED for every ID; a missing test never becomes a pass.

## 1. Color and effects

1. **Purple-to-blue gradient doing all the branding** → Pick colors that fit your product and audience.

2. **Big “aurora” glow behind every hero** → Keep a glow only when it supports the focal point.

3. **Competing accent colors obscure hierarchy or state** → Give colors clear roles; multiple brand accents are fine when hierarchy and status remain understandable.

4. **Blurred glass panels everywhere** → Use transparency only when showing layers matters.

5. **Heavy shadow on every card and button** → Use shadows to show meaningful depth or priority.

6. **The same huge rounded corners on every element** → Set a small, consistent radius scale for different component types.

7. **Gradient text used for every heading or metric** → Use size, weight, or a solid accent color for emphasis.

8. **Layered gradients make actions and surfaces difficult to distinguish** → Use consistent effect roles and readable contrast; keep multiple gradients when the approved direction supports them.

9. **Dark mode chosen only because it “looks futuristic”** → Match the theme to your users, content, and brand.

10. **Blur, grain, mesh, and glow layered across the whole page** → Keep backgrounds quiet enough that content stays clear.

## 2. Layouts and grouping

11. **Centered hero with a vague headline and one button** → Say who the product helps and what it helps them do.

12. **Exactly three identical feature cards** → Choose a layout that fits the number and importance of your features.

13. **Every feature gets an icon, heading, and two lines** → Give each feature the space and explanation it actually needs.

14. **A repeated column layout obscures different content relationships** → Reuse layouts where they work; change them when grouping, order, or comparison needs a different structure.

15. **Cards placed inside other cards** → Remove containers that don’t help users understand grouping.

16. **A card around every paragraph or group of text** → Use spacing and headings when a border is unnecessary.

17. **All cards are the same size despite different importance** → Make the main feature or action visually prominent.

18. **Metric tiles used instead of explaining what the numbers mean** → Add context, definitions, and useful visualizations.

19. **Repeated image-and-text sections make every feature seem equally important** → Adjust emphasis to the content; keep a repeated layout when it improves scanning and comparison.

20. **Large empty sections that don’t guide attention** → Use whitespace deliberately, with a clear reading order.

## 3. Typography

21. **Typography lacks clear roles or does not suit the reading context** → Choose readable typography and clear roles; system fonts can be an intentional, effective choice.

22. **Every text element uses the same size and weight** → Create a small, consistent type scale for headings, body text, and labels.

23. **Too many font families competing on one page** → Limit the typefaces and give each a clear role.

24. **Every section starts with a tiny ALL CAPS label** → Use uppercase labels sparingly; they don’t need to introduce every section.

25. **Widely spaced letters in tiny labels** → Make labels easy to read at normal viewing size.

26. **Important details hidden in tiny, pale metadata** → Increase the size or contrast, or remove details users don’t need.

27. **Very thin, low-contrast text over a gradient or dark surface** → Use stronger text weight and contrast.

28. **Long paragraphs with cramped line spacing** → Give body text enough space to read comfortably.

29. **Manual line breaks that make headlines awkward on mobile** → Let text reflow naturally at smaller widths.

30. **All-caps navigation or button text everywhere** → Use normal sentence case unless uppercase is part of a deliberate, readable style.

## 4. Icons and symbols

31. **Emoji navigation is ambiguous or inconsistent across devices** → Use recognizable, labeled navigation; keep intentional emoji when they remain understandable in the target context.

32. **Mixed icon styles create inconsistent meanings or hierarchy** → Keep icons coherent within each role; a separate illustrative style may intentionally differ from control icons.

33. **Sparkles or magic wands attached to ordinary actions** → Reserve AI symbols for real AI features.

34. **The same icon-in-a-colored-square treatment for every feature** → Use icons only when they help users understand the feature.

35. **An icon communicates conflicting action meanings** → Use consistent symbols for the same action and distinct labels or symbols where meanings otherwise collide.

36. **Important actions shown only as unlabeled icons** → Add a visible text label where the meaning may be unclear.

37. **Essential navigation labels are discoverable only by pointer hover** → Provide visible labels or a usable labeled navigation alternative; tooltips must also work with focus and touch where needed.

38. **An icon where a direct text label would be clearer** → Prefer the words users are looking for.

39. **Decorative icons added to every heading and bullet** → Remove icons that don’t add meaning.

40. **Unfamiliar symbols such as stars or hearts with no explanation** → Label the action or test whether people understand the icon.

## 5. Images and evidence

41. **Random 3D robots or characters with no connection to the brand** → Use imagery that relates to the product or its audience.

42. **Abstract artwork distracts from the message or conflicts with the brand** → Keep artwork that supports brand or composition; replace or remove distracting decoration.

43. **Fake interface screenshots with garbled or meaningless text** → Show the real product, or label a mockup clearly.

44. **Generated images with visible visual mistakes** → Review every image at full size before using it.

45. **Stock photos unrelated to the product or audience** → Choose images that match the real context of use.

46. **Different visual styles for every illustration** → Set a consistent art direction.

47. **Decorative charts with impossible or meaningless values** → Use real data or clearly mark example data.

48. **A wall of logos with no explanation of the relationship** → Show only genuine partners or integrations, with context.

49. **Generic avatars presented as real people** → Use approved real photos or label illustrations as fictional.

50. **The page makes a product claim without an understandable example** → Show appropriate evidence such as a real screenshot, demonstration, portfolio example, or documented outcome; a screenshot is not required for every kind of site.

## 6. Copy and credibility

51. **A headline like “Unlock the future” with no concrete benefit** → Explain the product’s value in plain language.

52. **“AI-powered” repeated in every feature description** → Explain what the feature actually does for the user.

53. **Hype words like “seamless,” “effortless,” and “revolutionary” everywhere** → Use specific descriptions instead.

54. **Feature cards with the same generic copy structure** → Write to the real differences between features.

55. **Copy that would fit any company after changing the name** → Mention your audience, use case, and product details.

56. **Big performance claims with no definition or evidence** → Show how the number was measured and what it means.

57. **Testimonials with generic names or no permission** → Use genuine, approved testimonials—or none.

58. **Commercial terms or relevant limits are unclear where users must choose** → Explain applicable pricing, usage limits, renewal terms, or access requirements using approved information; do not invent plans.

59. **Trust, security, or compliance badges without proof** → Display only claims you can substantiate.

60. **No clear way to learn who runs the service or contact them** → Provide appropriate company, support, and policy information.

## 7. Interactions and forms

61. **An action label leaves its outcome ambiguous in context** → Use an outcome-specific label when needed; familiar labels such as Get started are fine when surrounding context makes the next step clear.

62. **Primary and secondary actions look equally important** → Make the main action visually clear.

63. **Links or buttons that do nothing** → Connect every visible action to a real destination or behavior.

64. **Controls that look interactive but are only decoration** → Make them work, or style them as non-interactive.

65. **A control provides no feedback for its relevant states** → Make focus, activation, availability, and pending states understandable; add hover treatment on devices that support hover.

66. **Every click opens another modal** → Use the interaction that best fits the task and its context.

67. **Forms that use placeholder text instead of persistent labels** → Give each field a label users can still see while typing.

68. **Errors like “Something went wrong” with no next step** → Explain the problem and how to fix or retry.

69. **Empty areas that only say “No data”** → Explain why they’re empty and what the user can do next.

70. **Destructive actions with no warning or recovery option** → Make the consequence clear and offer confirmation or undo where appropriate.

## 8. Accessibility

71. **Text lacks sufficient contrast for its applicable role** → Measure actual foreground/background contrast. WCAG 1.4.3 AA requires 4.5:1 for normal text and 3:1 for large text, with defined exceptions.

72. **Gradient text that becomes hard to read in parts** → Keep text on a predictable background and verify contrast across the whole line.

73. **Text loses information or functionality when resized** → Inspect text resizing to 200% under WCAG 1.4.4, including its exceptions; inspect reflow separately under check 88.

74. **Keyboard focus is missing or nearly invisible** → Provide a clear focus indicator.

75. **Custom controls that can’t be used by keyboard** → Make key actions work with keyboard input.

76. **Pointer targets are difficult to activate without hitting neighbors** → Check WCAG 2.5.8 AA: 24 by 24 CSS pixels or an applicable spacing, equivalent-control, inline, user-agent, or essential exception. Larger targets can improve usability.

77. **Actions that require hover to discover or use** → Make them available to touch and keyboard users too.

78. **Status or errors communicated by color alone** → Add text, a symbol, or another clear cue.

79. **Automatic motion or updates distract without usable controls** → Apply WCAG 2.2.2 pause/stop/hide rules to qualifying automatic content; honor reduced-motion preferences as separate design guidance, not a blanket AA requirement.

80. **Informative images have missing or unhelpful alternatives** → Describe information or function in context; use empty alt for purely decorative HTML images and appropriate exclusion from assistive technology.

## 9. Consistency and responsive behavior

81. **Spacing changes randomly between sections** → Define a spacing scale and use it consistently.

82. **Elements don’t line up from one section to the next** → Use a grid or clear alignment rules.

83. **The same component looks different on different pages** → Reuse shared styles and components.

84. **Icon size or stroke weight changes without a reason** → Standardize icon sizing and style.

85. **Buttons, pills, and cards have unrelated shapes** → Set consistent shape rules for each component type.

86. **Labels switch between different terms or capitalization** → Use the same product language everywhere.

87. **The desktop layout is just squeezed onto a phone** → Design a layout that works at narrow widths.

88. **Mobile or enlarged layouts require unintended horizontal page scrolling** → Inspect reflow at 320 CSS pixels for vertically scrolling content; preserve legitimate two-dimensional regions such as tables and maps without forcing surrounding prose to scroll horizontally.

89. **Sticky surfaces obscure content, focused controls, or actions** → Check reading and keyboard navigation with fixed headers and overlays; preserve visibility and apply WCAG 2.4.11 where focus is obscured.

90. **Layouts break with longer names, labels, or enlarged text** → Test realistic content, narrow screens, and zoom.

## 10. Product completeness

91. **Product claims imply unavailable capabilities are already usable** → Match claims to real capabilities; distinguish explicitly labeled previews, roadmap items, and prototypes.

92. **Demo data looks real but isn’t labelled** → Mark sample data clearly.

93. **Form errors erase what the user entered** → Preserve input and explain what needs correcting.

94. **The interface exposes raw server errors or technical stack traces** → Show a useful message and keep technical detail out of the user flow.

95. **Actions appear to succeed but don’t save after a refresh** → Confirm that important changes persist.

96. **Slow requests give no progress feedback** → Show a loading state or progress where it helps.

97. **Empty, offline, or failed states leave users stuck** → Provide a next step, retry, or clear explanation.

98. **Account, permission, or expired-session cases are ignored** → Handle them with clear guidance.

99. **Direct links, refreshes, or unknown routes lead to broken pages** → Check routing, 404 pages, and reload behavior.

100. **Large images or heavy effects make the site feel slow** → Compress assets and keep interactions responsive.

## 11. Wayfinding

101. **A page has no clear job or primary task** → Give it a title and opening that tell users what they can do here.

102. **Navigation follows internal teams or code modules** → Group links around the tasks users came to complete.

103. **Users cannot tell where they are** → Mark the active destination and show local context where the hierarchy needs it.

104. **Shareable URLs disclose sensitive input or credentials** → Allowlist safe share state; avoid exposing tokens, private queries, or confidential values in URLs and referrer data.

105. **Back navigation loses useful search or detail context** → Restore the previous state when users would expect to continue where they left off.

106. **Useful views cannot be bookmarked or shared when the task needs it** → Represent safe, durable view state in the URL or an authorized share mechanism; avoid private state and enforce access on the destination.

107. **Search does not say what it searches** → Name its scope and keep the submitted query visible with the results.

108. **Applied filters are hard to see or clear** → Show selected filters, result count, and a clear reset path.

109. **Zero search results look like an empty account** → Explain whether filters hid results or no records exist, then offer a relevant next action.

110. **Help is far from the decision that needs it** → Put concise explanations beside unfamiliar choices and link to deeper guidance only when needed.

## 12. Interaction reliability

111. **A disabled action hides its prerequisite** → Explain the missing permission, input, or dependency near the action and provide a useful next step where possible.

112. **Repeated submission creates duplicate operations** → Show the pending state, prevent accidental resubmission, and verify server-side duplicate protection when the operation requires it.

113. **A progress bar advances without measured progress** → Show actual steps or a truthful waiting state; do not invent percentages.

114. **A long task has no safe way to stop or leave** → Explain cancellation behavior and let users stop work when the product supports it.

115. **An older async response overwrites a newer query or selection** → Cancel or ignore stale results so the visible response matches the latest input and selected context.

116. **An optimistic change stays visible after the server rejects it** → Roll it back or mark it unsaved and explain the conflict.

117. **A destructive prompt hides what will be affected** → Name the record, range, or people affected before confirmation.

118. **A success toast is the only record of a lasting change** → Update the page's durable state and identify what changed.

119. **Undo claims to reverse a change it cannot actually restore** → Check the permitted undo window and restored state; explain limits and never promise reversal for irreversible operations.

120. **Account or organization switching retains the previous context data** → Clear or isolate prior-context caches and selection; verify loading and access states under the newly selected account or organization.

## 13. Data meaning

121. **A chart title omits the subject or measure** → Name what is being measured and whose or which data is shown.

122. **Axes omit units, time range, or scale** → Label them so a screenshot or export still makes sense.

123. **A chart scale makes a difference look misleadingly large** → Choose the scale for the analytical task. Bars generally need a zero baseline; justified non-zero line-chart scales must remain clear and explicit.

124. **Zero, missing, unavailable, filtered, and not applicable share one display** → Give each state a distinct label or treatment.

125. **A value is detached from its currency, unit, or magnitude** → Keep “USD,” “per month,” “millions,” or equivalent beside the number.

126. **Displayed precision exceeds what the source supports** → Match rounding to the source and make exact underlying values inspectable when relevant.

127. **Forecasts, estimates, examples, and observed values look identical** → Label each data class in the value and its visualization.

128. **A KPI shows a change without its denominator or comparison window** → Name the baseline and the period used to calculate the change.

129. **Dates omit the reporting period or relevant time zone** → State the period and zone where either can change interpretation.

130. **A source link opens only a generic home page** → Link to the exact record, version, or passage used for the displayed result.

## 14. Accessibility mechanics

131. **The page is a visual stack with no semantic structure** → Use landmarks, headings, lists, buttons, links, and form controls for their real roles.

132. **Keyboard users must tab through the whole header on every page** → Provide a visible-on-focus skip link to the main content.

133. **A modal loses focus containment or returns focus to the wrong place** → Use the APG dialog pattern: appropriate initial focus, contained Tab order, a close mechanism, and return to the trigger or a logical next task target.

134. **Keyboard focus jumps in an order that contradicts the page** → Keep focus order aligned with the reading and task sequence.

135. **Route changes leave a stale document title or unclear focus** → Update the page title and provide a predictable focus location after navigation.

136. **Important status changes are visible but not announced** → Expose progress, success, and error updates as accessible status messages without stealing focus.

137. **An error is visually near a field but not programmatically connected** → Associate the message with the input and identify the invalid field on submit.

138. **Repeated icon controls have indistinguishable accessible names** → Include the affected item in each control's name, such as “Archive Q3 report.”

139. **A data grid looks tabular but has no header relationships** → Use a semantic table or fully implement an accessible grid with named rows and columns.

140. **User text-spacing overrides clip content or hide actions** → Check WCAG 1.4.12: line height 1.5, paragraph spacing 2, letter spacing 0.12, and word spacing 0.16 times font size without loss, subject to language/script exceptions. These are override checks, not mandatory default styles.

## 15. Release resilience

141. **Nonessential scripts delay the first useful page content** → Keep essential content and loading feedback available while optional code loads; use progressive rendering appropriate to the application.

142. **Web fonts cause text to jump or disappear while loading** → Set a readable fallback and avoid layout shifts when fonts arrive.

143. **Images move the page when they load** → Reserve their dimensions and test at the actual rendered size.

144. **A site only works on a fast developer laptop** → Inspect the main journey with throttled CPU and network, then fix blockers users can feel.

145. **Unexpected browser errors or failed requests disrupt the main journey** → Inspect relevant console and network failures, reproduce their effect, and distinguish expected denials from actual defects.

146. **A third-party widget blocks the whole page when it fails** → Provide a useful fallback and keep unrelated tasks usable.

147. **Another tab or user can change a record without the page noticing** → Detect stale edits and ask users to reload or resolve the conflict before overwriting newer work.

148. **Locale formatting or text direction changes the meaning of content** → Use supported locale conventions for numbers, dates, currency, and direction; inspect the actual locales the product offers.

149. **An error or permission page drops the user's place** → Keep enough context to retry, request access, or return to the prior task.

150. **Analytics or diagnostics capture secrets or private field contents** → Inspect the intended event payloads and redaction rules using synthetic inputs; collect only approved data and keep sensitive values out of URLs and logs.

## Use the checks deliberately

Evaluate applicability before inspecting. Keep one remediation finding for a single root defect even when several IDs apply. Report observed user impact and scope; do not calculate an AI probability or imply full accessibility conformance. See review-guide.md for the evidence protocol.
