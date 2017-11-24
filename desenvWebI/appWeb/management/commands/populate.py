# coding=utf-8
from django.core.management.base import BaseCommand
from appWeb.models.aluno_model import AlunoModel
from appWeb.models.curso_model import CursoModel
from appWeb.models.funcionario_model import FuncionarioModel
from appWeb.models.tipo_funcionario_model import TipoFuncionarioModel
from appWeb.models.ocorrencia_model import OcorrenciaModel
from appWeb.models.tipo_ocorrencia_model import TipoOcorrenciaModel
from appWeb.models.tipo_oferta_model import TipoOfertaModel
from appWeb.models.turma_model import TurmaModel

from django.contrib.auth.models import User


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _populate_tipos(self):
        tipo_oferta1, created = TipoOfertaModel.objects.get_or_create(
            nome=u'Anual',
        )

        tipo_oferta2, created = TipoOfertaModel.objects.get_or_create(
            nome=u'Semestral',
        )
        tipo_funcionario1, created = TipoFuncionarioModel.objects.get_or_create(
            nome=u'NUPE',
        )

        tipo_funcionario2, created = TipoFuncionarioModel.objects.get_or_create(
            nome=u'Professor',
        )

        tipo_funcionario3, created = TipoFuncionarioModel.objects.get_or_create(
            nome=u'Porteiro',
        )

        tipo_ocorrencia1, created = TipoOcorrenciaModel.objects.get_or_create(
            nome=u'Entrada',
        )

        tipo_ocorrencia2, created = TipoOcorrenciaModel.objects.get_or_create(
            nome=u'Saída',
        )
        nupe, created = FuncionarioModel.objects.get_or_create(
            matricula='1234567890',
            funcao=tipo_funcionario1,
            username=u'vaniavania',
            email=u'vaniavania@vaniavania.com',
            first_name=u'Vania',
            last_name=u'Vania'
        )
        nupe.set_password(u'vaniavania')
        nupe.save()
        professor, created = FuncionarioModel.objects.get_or_create(
            funcao=tipo_funcionario2,
            matricula='1234567890',
            username=u'ivomarcos',
            email=u'ivoriegel@ivoriegel.com',
            first_name=u'Ivo',
            last_name=u'Marcos Riegel',
        )
        professor.set_password(u'ivomarcos')
        professor.save()
        porteiro, created = FuncionarioModel.objects.get_or_create(
            funcao=tipo_funcionario3,
            matricula='1234567890',
            username=u'joaojoao',
            email=u'joaojoao@joaojoao.com',
            first_name=u'Joao',
            last_name=u'Joao Riegel',
        )
        porteiro.set_password(u'joaojoao')
        porteiro.save()
        curso1, created = CursoModel.objects.get_or_create(
            nome='Informática',
            descricao='Informática High Tech',
            duracao='4',
            oferta=tipo_oferta1,
            coordenador=professor,
        )
        curso2, created = CursoModel.objects.get_or_create(
            nome='Agropecuária',
            descricao='Agropecuária Low Tech',
            duracao='3',
            oferta=tipo_oferta2,
            coordenador=professor,
        )
        turma1, created = TurmaModel.objects.get_or_create(
            curso=curso1,
            nome='1 Info',
            descricao='Turma 1',
            ano='2027',
        )
        turma2, created = TurmaModel.objects.get_or_create(
            curso=curso2,
            nome='2 Agro',
            descricao='Turma 2',
            ano='2027',
        )
        aluno, created = AlunoModel.objects.get_or_create(
            turma=turma1,
            curso=curso1,
            nome='Vinicius Oliveira',
            email='vini@vini.com',
            matricula='1234567890',
            nome_pai='Sergio Marcos',
            nome_mae='Adriane Galisteu',
            telefone_responsavel=123456789,
        )

        aluno, created = AlunoModel.objects.get_or_create(
            turma=turma1,
            curso=curso1,
            nome='Eduardo Silva II',
            email='edu@dudu.com',
            matricula='1234567890',
            nome_pai='Eduardo Marcos I',
            nome_mae='Mônica Galisteu',
            telefone_responsavel=123456789,
        )

        aluno, created = AlunoModel.objects.get_or_create(
            turma=turma1,
            curso=curso1,
            nome='Emanuel Silva III',
            email='manu@mano.com',
            matricula='1234567890',
            nome_pai='Eduardo Silva II',
            nome_mae='Mônica Galisteu II',
            telefone_responsavel=123456789,
        )

    def handle(self, *args, **options):
        self._populate_tipos()
