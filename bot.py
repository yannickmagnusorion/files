from mechanize import Browser
br=Browser()
br.set_handle_robots(False)
br.open("http://myaplication.esy.es/Pessoas/create.php")
print list(br.forms())
#for form in br.forms():
#    print form.name
"""br.select_form(nr=0)
br.form['nm_usuario']='SOBRINHO'
br.form['nm_senha_atual']='amelia2016'
br.form['nm_nova_senha']='amelia2008'
br.form['nm_repetir_senha']='amelia2008'
br.submit()
"""
