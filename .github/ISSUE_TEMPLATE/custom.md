name: Custom
description: Use this for any other issues. Please do NOT create blank issues
title: "[OTHER]"
labels: ["triage"]
body:
  - type: markdown
    attributes:
      value: "# Other issue"
  - type: textarea
    id: issuedescription
    attributes:
      label: What would you like to share?
      description: Provide a clear and concise explanation of your issue.
    validations:
      required: true
  - type: textarea
    id: extrainfo
    attributes:
      label: Additional information
      description: Is there anything else we should know about this issue?
    validations:
      required: false
  - type: markdown
    attributes:
      value: |
        You can also join our Discord community [here](https://discord.gg/6A3WmNCmsk)
        Feel free to check out other repositories of the Keribium [here](https://github.com/Keribium)