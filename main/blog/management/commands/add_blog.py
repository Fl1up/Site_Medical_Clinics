from django.core.management.base import BaseCommand

from main.blog.models import Blog


class Command(BaseCommand):
    def handle(self, *args, **options):
        Blog.objects.all().delete(),

        Blog.objects.create(
            title="О последних новостях в мире медицины",
            img="blog/blog_1.png",
            description="В этом блоге Вы найдете самые свежие и интересные новости из сферы медицины."
                        " Мы будем рассказывать о новых методах лечения, последних исследованиях в области "
                        "медицины, а также делиться полезными советами для здоровья и профилактики заболеваний."
                        " Присоединяйтесь к нам и будьте в курсе всех событий в мире медицины!")
        Blog.objects.create(
            title="О здоровом образе жизни и физической активности",
            img="blog/blog_2.png",
            description="Здоровый образ жизни - это не просто модное понятие, а неотъемлемая часть нашего"
                        " счастья и благополучия. В этом блоге мы будем рассказывать о различных аспектах"
                        " здорового образа жизни, начиная от правильного питания и заканчивая физическими "
                        "упражнениями. Мы поделимся с Вами полезными советами, рецептами здоровой пищи, а "
                        "также расскажем о самых эффективных способах достижения физической формы.")
        Blog.objects.create(
            title="О женском здоровье и самочувствии",
            img="blog/blog_3.png",
            description="В этом блоге мы будем говорить обо всех важных аспектах женского здоровья. Мы "
                        "поделимся советами по уходу за здоровьем женщин, расскажем о гормональных изменениях,"
                        " связанных с различными фазами жизни, и о методах лечения и профилактики женских "
                        "заболеваний. Здесь вы найдете полезную и достоверную информацию, которая поможет"
                        " вам сохранить свое здоровье на протяжении всей жизни.")
        Blog.objects.create(
            title="О психологическом здоровье и психотерапии",
            img="blog/blog_4.png",
            description="Психологическое здоровье является неотъемлемой частью нашего общего "
                        "благополучия. В этом блоге мы будем говорить о различных аспектах психического"
                        " здоровья, таких как стресс, депрессия, тревожность, и о том, как справиться с "
                        "ними. Мы поделимся информацией о психотерапевтических методах и техниках, которые "
                        "помогут вам развивать эмоциональное благополучие и осознанность.")
        Blog.objects.create(
            title="О методах альтернативной медицины и натуральных лечебных подходах",
            img="blog/blog_5.png",
            description="В этом блоге мы будем рассказывать о различных методах альтернативной медицины, "
                        "таких как траволечение, аюрведа, гомеопатия и другие натуральные подходы к "
                        "оздоровлению. Мы поделимся с Вами информацией о принципах этих методов, их "
                        "эффективности и противопоказаниях. Здесь вы найдете советы по использованию "
                        "альтернативных методов для поддержания здоровья и профилактики заболеваний.")
        Blog.objects.create(
            title='О здоровье детей и семейной медицине',
            img="blog/blog_6.png",
            description="В этом блоге мы будем говорить о всех аспектах здоровья детей, начиная с "
                        "новорожденных и заканчивая подростками. Мы поделимся советами по уходу за "
                        "детским здоровьем, расскажем о прививках, правильном питании для детей и "
                        "методах лечения детских заболеваний. Мы также обсудим важные вопросы о семейной "
                        "медицине и ответим на ваши вопросы о здоровье вашего ребенка.")
