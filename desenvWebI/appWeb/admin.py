from django.contrib import admin
from .models import AlunoModel
from .models import CursoModel
from .models import FuncionarioModel
from .models import PermissaoModel
from .models import TipoFuncionarioModel
from .models import TipoOfertaModel
from .models import TipoPermissaoModel
from .models import TurmaModel

# Register your models here.

admin.site.register(AlunoModel)
admin.site.register(CursoModel)
admin.site.register(FuncionarioModel)
admin.site.register(PermissaoModel)
admin.site.register(TipoFuncionarioModel)
admin.site.register(TipoOfertaModel)
admin.site.register(TipoPermissaoModel)
admin.site.register(TurmaModel)