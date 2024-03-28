---
name: Help me
about: Get help with OutsetaPy
title: ''
labels: help wanted
assignees: ''

---

**Describe the problem**
A clear and concise description of what you're trying to accomplish, and where you're having difficulty.

**Code snippet(s)**
Here is some code that can be easily used to reproduce the problem or understand what I need help with.

- [ ] I know that if I don't provide sample code that allows someone to quickly step into my shoes, I may not get the help I want or my issue may be closed.

```python
import asyncio
from outsetapy import OutsetaApiClient

outseta = OutsetaApiClient(...)

async def main():
	print('Accounts:')
	accounts = await outseta.crm.accounts.get_all()

asyncio.run(main())
```
