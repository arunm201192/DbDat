class check_privilege_grant_any_role():
	"""
	check_privilege_grant_any_role:
	The	Oracle database GRANT ANY ROLE keyword provides the grantee the capability
	to grant any single role to any grantee in the catalog of the database.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Grant Any Role'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='GRANT ANY ROLE' AND grantee NOT IN ('DBA','SYS','DATAPUMP_IMP_FULL_DATABASE','IMP_FULL_DATABASE','SPATIAL_WFS_ADMIN_USR','SPATIAL_CSW_ADMIN_USR')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Grant Any Role granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Grant Any Role.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
