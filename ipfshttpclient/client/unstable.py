# -*- coding: utf-8 -*-
from __future__ import absolute_import

from . import base


class LogSection(base.SectionBase):
	def level(self, subsystem, level, **kwargs):
		r"""Changes the logging output of a running daemon.
		
		**This API is subject to future change or removal!**
		
		.. code-block:: python

			>>> client.unstable.log.level("path", "info")
			{'Message': "Changed log level of 'path' to 'info'\n"}

		Parameters
		----------
		subsystem : str
			The subsystem logging identifier (Use ``"all"`` for all subsystems)
		level : str
			The desired logging level. Must be one of:

			 * ``"debug"``
			 * ``"info"``
			 * ``"warning"``
			 * ``"error"``
			 * ``"fatal"``
			 * ``"panic"``

		Returns
		-------
			dict : Status message
		"""
		args = (subsystem, level)
		return self._client.request('/log/level', args,
		                            decoder='json', **kwargs)

	def ls(self, **kwargs):
		"""Lists the logging subsystems of a running daemon.
		
		**This API is subject to future change or removal!**
		
		.. code-block:: python

			>>> client.unstable.log.ls()
			{'Strings': [
				'github.com/ipfs/go-libp2p/p2p/host', 'net/identify',
				'merkledag', 'providers', 'routing/record', 'chunk', 'mfs',
				'ipns-repub', 'flatfs', 'ping', 'mockrouter', 'dagio',
				'cmds/files', 'blockset', 'engine', 'mocknet', 'config',
				'commands/http', 'cmd/ipfs', 'command', 'conn', 'gc',
				'peerstore', 'core', 'coreunix', 'fsrepo', 'core/server',
				'boguskey', 'github.com/ipfs/go-libp2p/p2p/host/routed',
				'diagnostics', 'namesys', 'fuse/ipfs', 'node', 'secio',
				'core/commands', 'supernode', 'mdns', 'path', 'table',
				'swarm2', 'peerqueue', 'mount', 'fuse/ipns', 'blockstore',
				'github.com/ipfs/go-libp2p/p2p/host/basic', 'lock', 'nat',
				'importer', 'corerepo', 'dht.pb', 'pin', 'bitswap_network',
				'github.com/ipfs/go-libp2p/p2p/protocol/relay', 'peer',
				'transport', 'dht', 'offlinerouting', 'tarfmt', 'eventlog',
				'ipfsaddr', 'github.com/ipfs/go-libp2p/p2p/net/swarm/addr',
				'bitswap', 'reprovider', 'supernode/proxy', 'crypto', 'tour',
				'commands/cli', 'blockservice']}

		Returns
		-------
			dict : List of daemon logging subsystems
		"""
		return self._client.request('/log/ls', decoder='json', **kwargs)

	def tail(self, **kwargs):
		r"""Reads log outputs as they are written.
		
		**This API is subject to future change or removal!**
		
		This function returns an iterator that needs to be closed using a
		context manager (``with``-statement) or using the ``.close()`` method.
		
		.. code-block:: python

			>>> with client.unstable.log.tail() as log_tail_iter:
			...     for item in log_tail_iter:
			...         print(item)
			...
			{"event":"updatePeer","system":"dht",
			 "peerID":"QmepsDPxWtLDuKvEoafkpJxGij4kMax11uTH7WnKqD25Dq",
			 "session":"7770b5e0-25ec-47cd-aa64-f42e65a10023",
			 "time":"2016-08-22T13:25:27.43353297Z"}
			{"event":"handleAddProviderBegin","system":"dht",
			 "peer":"QmepsDPxWtLDuKvEoafkpJxGij4kMax11uTH7WnKqD25Dq",
			 "session":"7770b5e0-25ec-47cd-aa64-f42e65a10023",
			 "time":"2016-08-22T13:25:27.433642581Z"}
			{"event":"handleAddProvider","system":"dht","duration":91704,
			 "key":"QmNT9Tejg6t57Vs8XM2TVJXCwevWiGsZh3kB4HQXUZRK1o",
			 "peer":"QmepsDPxWtLDuKvEoafkpJxGij4kMax11uTH7WnKqD25Dq",
			 "session":"7770b5e0-25ec-47cd-aa64-f42e65a10023",
			 "time":"2016-08-22T13:25:27.433747513Z"}
			{"event":"updatePeer","system":"dht",
			 "peerID":"QmepsDPxWtLDuKvEoafkpJxGij4kMax11uTH7WnKqD25Dq",
			 "session":"7770b5e0-25ec-47cd-aa64-f42e65a10023",
			 "time":"2016-08-22T13:25:27.435843012Z"}
			…

		Returns
		-------
			iterable
		"""
		return self._client.request('/log/tail', decoder='json',
		                            stream=True, **kwargs)



class RefsSection(base.SectionBase):
	def __call__(self, multihash, **kwargs):
		"""Returns a list of hashes of objects referenced by the given hash.
		
		**This API is subject to future change or removal!** You likely want to
		use :meth:`~ipfshttpclient.object.links` instead.
		
		.. code-block:: python
			
			>>> client.unstable.refs('QmTkzDwWqPbnAh5YiV5VwcTLnGdwSNsNTn2aDxdXBFca7D')
			[{'Ref': 'Qmd2xkBfEwEs9oMTk77A6jrsgurpF3ugXSg7 … cNMV', 'Err': ''},
			 …
			 {'Ref': 'QmSY8RfVntt3VdxWppv9w5hWgNrE31uctgTi … eXJY', 'Err': ''}]
		
		Parameters
		----------
		multihash : str
			Path to the object(s) to list refs from
		
		Returns
		-------
			list
		"""
		args = (multihash,)
		return self._client.request('/refs', args, decoder='json', **kwargs)


	def local(self, **kwargs):
		"""Displays the hashes of all local objects.
		
		**This API is subject to future change or removal!**
		
		.. code-block:: python
			
			>>> client.unstable.refs.local()
			[{'Ref': 'Qmd2xkBfEwEs9oMTk77A6jrsgurpF3ugXSg7 … cNMV', 'Err': ''},
			 …
			 {'Ref': 'QmSY8RfVntt3VdxWppv9w5hWgNrE31uctgTi … eXJY', 'Err': ''}]
		
		Returns
		-------
			list
		"""
		return self._client.request('/refs/local', decoder='json', **kwargs)



class Section(base.SectionBase):
	"""
	Features that are subject to change and are only provided for convinience
	"""
	log  = base.SectionProperty(LogSection)
	refs = base.SectionProperty(RefsSection)