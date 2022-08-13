from aiogram import types

from loader import dp


@dp.message_handler(text="/duolar")
async def show_menu(message: types.Message):
    msg = f"<b>Duolar:</b>\n\n"
    msg+="""<b>1. Иймон калимаси
'لاَ إِلَهَ إِلاَّ اللهُ وَحْدَهُ لاَ شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ'

«Лаа илаҳа иллаллоҳу ваҳдаҳу лаа шарийка лаҳу, лаҳул мулку ва лаҳул ҳамду ва ҳува ъалаа кулли шай`ин қодийр»

Маъноси: “Аллоҳдан бошқа илоҳ йўқ, У ёлғиз, Унинг шериги ҳам йўқ, бутун мулк Уники, ҳамд ҳам Унга хос ва У ҳар бир нарсага қодирдир”

2. Аллоҳдан паноҳ сўраш дуоси
'اللهُمَّ عَافِنِي فِي بَدَنِي، اللهُمَّ عَافِنِي فِي سَمْعِي، اللهُمَّ عَافِنِي فِي بَصَرِي، لا إلَهَ إلاَّ أنْتَ. اللهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الكُفْرِ وَالفَقْرِ، اللهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ عَذَابِ القَبْرِ لاَ إِلَهَ إِلاَّ أَنْتَ'

«Аллоҳумма ъафиний фий баданий, Аллоҳумма ъафиний фий самъий, Аллоҳумма ъафиний фий басорий, лаа илаҳа илла анта. Аллоҳумма инний аъузу бика минал куфри вал фақри, Аллоҳумма инний аъузу бика мин ъазабил қобр, лаа илаҳа илла анта»

Маъноси: “Аллоҳим, баданимни, қулоғимни ва кўзимни офиятда қил. Эй Раббим, Сенинг номинг ила куфрдан, камбағалликдан ва қабр азобидан паноҳ тилайман. Сендан бошқа илоҳ йўқ”

3. Аллоҳдан офият сўраш дуоси
'اللَّهُمَّ إنِّي اسْألُكَ العَافِيَةَ فِي الدُّنْيَا وَالآخِرَةِ، اللَّهُمَّ إنِّي اسْألُكَ العَفْوَ وَالعَافِيَةَ فِي دِيْنِي وَدُنْيَايَ وَأهْلِي وَمَالِي، اللَّهُمَّ اسْتُرْ عَورَاتِي وَآمِنْ رَوْعَاتِي، اللَّهُمَّ احْفَظْنِي مِنْ بَيْنِ يَدَيَّ وَمِنْ خَلْفِي وَعَنْ يَمِينِي وَعَنْ شِمَالِي وَمِنْ فَوقِي وَأعُوذُ بِعَظَمَتِكَ أَنْ أُغْتَالَ مِنْ تَحْتِي'

«Аллоҳумма инний ас`алукал ъафийата фиддунйа вал ахироҳ. Аллоҳумма инний ас`алукал ъафва вал ъафийата фий дийний ва дунйайа ва аҳлий ва маалий. Аллоҳуммастур ъавротий ва амин равъатий. Аллоҳуммаҳфазний мин байни йадаййа ва мин холфий ва ъан йамийний ва ъан шималий ва мин фавқий ва аъузу биъазоматика ан уғтаала мин таҳтий»

Маъноси: “Аллоҳим, мен Сендан дунё ва охиратда офият сўрайман. Эй Раббим, динимда ва дунёимда, аҳлимда ва молимда авф ва офият сўрайман. Эй Раббим, авратимни бекит, хавфларимни омонликка айлантир. Эй Аллоҳим, мени олдимдан, орқамдан, ўнг томонимдан, чап томонимдан, устимдан сақлагин. Эй Раббим, остимдан ҳалок қилишингдан Сенинг азаматинг ила паноҳ тилайман”

4. Аллоҳдан ёрдам сўраш дуоси
'يَا حَيُّ يَا قَيُّومُ بِرَحْمَتِكَ أَسْتَغِيثُ، أَصْلِحْ لِي شَأْنِي كُلَّهُ، وَلاَ تَكِلْنِي إِلَى نَفْسِي طَرْفَةَ عَيْنٍ'

«Йа ҳаййу йа қоййуму бироҳматика астағийсу аслиҳ лий ша`ний куллаҳу ва ла такилний ила нафсий торфата ъайн»

Маъноси: “Эй ҳай-тирик ва қаййум сифатига эга бўлган Зот, Сендан ёрдам сўрайман. Шаънимни ҳар бир нарсада ислоҳ эт ва кўз юмиб очгунчалик муддат ҳам ўз ҳолимга ташлаб қўйма”

5. Истиғфор дуоси
'أسْتَغْفِرُ اللهَ الَّذِي لاَ إِلَهَ إِلاَّ هُوَ الحَيُّ القَيُّومُ وَأَتُوبُ إِلَيْهِ'

«Астағфируллоҳаллазий лаа илаҳа илла ҳувал ҳаййул қоййум ва атубу илайҳ»

Маъноси: "Ҳай ва қаййум сифатли Зотдан бошқа илоҳ йўқ ва Унга истиғфор айтаман, Унга тавба қиламан".

</b>"""
    await message.reply(msg)