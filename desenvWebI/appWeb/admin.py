from django.contrib import admin
from appWeb.models.aluno_model import AlunoModel
from appWeb.models.curso_model import CursoModel
from appWeb.models.funcionario_model import FuncionarioModel
from appWeb.models.ocorrencia_model import OcorrenciaModel
from appWeb.models.tipo_funcionario_model import TipoFuncionarioModel
from appWeb.models.tipo_oferta_model import TipoOfertaModel
from appWeb.models.tipo_ocorrencia_model import TipoOcorrenciaModel
from appWeb.models.turma_model import TurmaModel

# Register your models here.

admin.site.register(AlunoModel)
admin.site.register(CursoModel)
admin.site.register(FuncionarioModel)
admin.site.register(OcorrenciaModel)
admin.site.register(TipoFuncionarioModel)
admin.site.register(TipoOfertaModel)
admin.site.register(TipoOcorrenciaModel)
admin.site.register(TurmaModel)