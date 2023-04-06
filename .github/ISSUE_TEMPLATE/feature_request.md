name: General Feature Request
description: Have a new idea/feature for Keribium? Please suggest!
title: "[FEATURE] <description>"
labels: ["feature","triage"]
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      description: A brief description of the enhancement you propose, also include what you tried and what worked.
    validations:
      required: true
  - type: textarea
    id: screenshots
    attributes:
      label: Screenshots
      description: Please add screenshots if applicable
    validations:
      required: false
  - type: textarea
    id: extrainfo
    attributes:
      label: Additional information
      description: Is there anything else we should know about this idea?
    validations:
      required: false
  - type: markdown
    attributes:
      value: |
        You can also join our Discord community [here](https://discord.gg/6A3WmNCmsk)
        Feel free to check out other repositories of the Keribium [here](https://github.com/Keribium)