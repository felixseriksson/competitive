c = "0x30ee3e2413cb231813c6a4337006f264723d2e1531e0c40487f35d49c623cd5fc7d561b8dfd29e7bed1f993191d22f8ac63b6205bbde1bb59b2bfaf78248c2f49c12468a86404f3eee409d8298bd0cd50c54969acb3392d388a8b9bdaf77483ff5a958f495aec66d87e59af16ddaa52c3d0b4374ad101822e8a668423ac06aa4d86d4bc1cb6054361a47d39d61d2c7275d7c8d6a5ac0d4429735ab67fe1c0f52614f23fafd3e148c79dce01a58d775a74c327c66434a5242af7c974246399ca141141c3c6785567ba0c9feff11ea11514da75e15f86229de754c4eceec74598cd714afc2173e40944eb244bc0adf2ada8a416ce3fa741bf13d5c2de315392d06657618ba6c7711b4339ef9930ef0c5efa137403716db95c04f3ff53305f3b8a98914f7324eca0b08644c86354d6f58565dacb5c2aea435e81dcf80ff74b14816c8b6b0f6ff753be49222261d12076870e3af9408354365ba7f8aa87a36c021e098c2ce4d48b2a454bca0f2e249efaa7041dff455c586d48e8c508e08e73347385d3a391ddd8fb6acb3bcaed427051c7fa3ca9ac014add41c9bd3ae72dbeff2e57147c3d709d46b61e7923619259a22a942a4bf98a5af64be26988a75b9d73badbf36c32ed4450d5010c21317f33fb74e6dca8cd0e0e32e5692f115e894286185b55f6a3dbbc62ce01b901ae65a46eba40449457619e56ab92da6956716a153"
n = "0x99a9de29744e7596a10d91efbe20eefc7ebe10232b039f283fbc37c251005ac94d6dcc07a93e72b97154b3b65faf7c23005c2d38c8238b5a2b56519fe2339cb258665ea8682090186a25916b1e8573b60c802ebda9dc8e150efafe3182b11e9691bca1181e9359ef7d8a184120be0d522e398ec46335a0c79ae7cf3fb57a28ad31adbd5691cb64bff088c5b63e7a53f3c76e4ed9996dfb0cfbfbe50c8d147d28227e0563d03e7b7a5abbba73b158f93831c048885ade5de4150801fe622b77b116a8ec1cece67e66f72ccf5e0dab4a38314895e88846116c217f387e280a411b660cea8dff90145725293614f904d7de9838f3c0021c84d4e9a1646df207190dca89d20e486171ac178ade55c527a7cd853755e4ab4fbf6d382e77e26df20f14e4b59e1de400b9437d88e7fd99d4b445709ca85bf1e694707fb3da0bbb96034f864486bf7b8d3fa8657fcfc022ed7181deb36710c02d6c8b4d9c25f806d368123f521bcd84397530653bc14cfa083fe8dd3aa9eaf749061237bc12a8fd4a30ab9167e78130584be68f7a7b3b9d67460867fa1be3b0e287c2e26aa8549fe91b7c00646dd13d5ac88ed0a09241063ef2ddae59ce880b3ef2281e93cfb917ddfc11916b8dc8270d41bee9c224c2edc29764ba6b51757a149fbbc940cfff93183216aeb123d4964b701ab23e99f8f370cf20568a86a8ec4e4ccd7dd4fd440b5dabb5"
# print(int(n, 16))
mto3 = int.from_bytes(c, "big") + int.from_bytes(n, "big")
# mto3 = 627672338586937721995959108305620389381727839951021864185447659950054189557396048217908691112970010913619691900900136453730711075153952344965594261732860930160506827012091743091551350709465287761018111001300351285193650119556356647985103636617892560372606156887232242248120525281438038018326292721304257907172305528701724792873477943081209524733124834908658648833692015873957480820722925207731597093719416246402219136802340345789073081903871515782562074153524528596782344682361372176938341167952452990306686635775458423864616918300883437564308350621129210520941639852464168833773240582721561672748747748946185543808784456397682727281096148404451326380227972905851289499351035763714652065965633644641369194514558164942774604353131644357626803351279514092490447374682765242644185658277142459584601427112996161845325994920904772023436388168301207443184209203117036683842237690206942703302461202614829431598325952038086840520830431876070241178018112405278755101489032504287271236725902843045104595291548383297868548070336579695347186801725091661373811375558170834687141947242272081607837828670109592802230323009148096469974550021274799372727329826055179253226956196289070045106214482856954893546166512427104952102511011077760919660678408
# mto3 = 2^3 * 3 * 39857 * 656171164608201112723778245044388260303217167991216373729256738621879667266097180982333395130267802094173850579258491245505506221360062583073648984424380629668258636094968411123465713581747756313213604261589715822809931044689302431175936929332669042214046630126903933905504392036361281182651199623345395107480394000951029924556830191979252415649619091281182988385239748636748752645627833261965272822966497150649215880943477458778751831447290224827259613695549640586745892275678647181317314783635301400743790964965855458121761253043049148167520082859900404906856219163158467389431008127724909962228244880600423120790978222559904499503533620615002097477887586565566995236461010365927620478591834187053475753437871813548827270359380247256469799691479867706729105902228346800900914162168442243086326771450640374594724049854171132656994994781658185767435466378884759561099929843154843882821149361691828946398296777686569946434367898441167006609062933743632188303904199705914552061877360358118925779757997741193379402269714834382236481673780736613992744243543763574243694068003813719053781674350500531903879622785989178469251062152690451042400885066252664999484570042369251370635662580032945795328890902086526992438081778898897851131
print(mto3)