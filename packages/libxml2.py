class LibXmlPackage (Package):
	def __init__ (self):
		Package.__init__ (self,
			'libxml2',
			'2.9.0',
			configure_flags = [ '--with-python=no' ],
			sources = [
				'ftp://xmlsoft.org/%{name}/%{name}-%{version}.tar.gz',
				'patches/libxml290-darwin-build.patch'
			]
		)

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

LibXmlPackage ()

