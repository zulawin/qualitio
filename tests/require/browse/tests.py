# -*- coding: utf-8 -*-
from selenium import selenium
from config import settings
import unittest, time, base64

class BaseSeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 
                                 4444, 
                                 "*%s" % settings['browser'], 
                                 settings['hostname'])
        
        if settings['username']:
            self.selenium.addCustomRequestHeader("Authorization", "Basic %s" % 
                                                 base64.b64encode("%s:%s" % (settings['username'], settings['password'])).strip())
        self.selenium.start()

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)


class Test1HeaderpageVerifytext(BaseSeleniumTestCase):
    
    def test_1_headerpage_verifytext(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        sel.click("link=MeeGo")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.failUnless(sel.is_element_present("css=div.logo"))
        try: self.assertEqual("qualitiorequirements", sel.get_text("css=div.logo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.failUnless(sel.is_element_present("css=#notification.notify-wrapper-oneattime"))
        try: self.assertEqual("requirments", sel.get_text("link=requirments"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("store", sel.get_text("link=store"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # <tr>
        # 	<td>verifyText</td>
        # 	<td>link=execute</td>
        # 	<td>execute</td>
        # </tr>
        # <tr>
        # 	<td>verifyText</td>
        # 	<td>link=report</td>
        # 	<td>report</td>
        # </tr>
        # <tr>
        # 	<td>verifyText</td>
        # 	<td>link=settings</td>
        # 	<td>settings</td>
        # </tr>
        try: self.assertEqual("admin", sel.get_text("link=admin"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.failUnless(sel.is_element_present("css=#application-menu"))
        try: self.assertEqual("browse", sel.get_text("css=#application-menu ul li"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # <tr>
        # 	<td>verifyText</td>
        # 	<td>css=#application-menu ul li a</td>
        # 	<td>filter</td>
        # </tr>


class Test2TreeVerifyelements(BaseSeleniumTestCase):
    
    def test_2_tree_verifyelements(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        for i in range(60):
            try:
                if sel.is_text_present("MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Notebook"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#2 a ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#1 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=li#1 ins")
        sel.click("css=li#1 ins")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#2 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#4 a ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#4 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=li#4 ins")
	time.sleep(1)
        for i in range(60):
            try:
                if sel.is_element_present("link=Bootscreen"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=li#8 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test3Newreq(BaseSeleniumTestCase):
    
    def test_3_newreq(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(2)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 1")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test4Modreq(BaseSeleniumTestCase):
    
    def test_4_modreq(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
	time.sleep(3)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(2)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 2")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        time.sleep(2)
	sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        time.sleep(2)
	sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 2")
        sel.click("link=new requirement 2")
        for i in range(60):
            try:
                if "requirement: new requirement 2" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "mod requirement 3")
        sel.click("css=input.ui-button")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=mod requirement 3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=mod requirement 3")
        for i in range(60):
            try:
                if "requirement: mod requirement 3" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:requirement: mod requirement 3"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test5TestcasesDel(BaseSeleniumTestCase):
    
    def test_5_testcases_del(self):
        sel = self.selenium
        sel.set_timeout("10000")
        sel.open("/require/#requirement/13/details/")
        for i in range(60):
            try:
                if sel.is_text_present("qualitiorequirements"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "requirement: MeeGo" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if "requirement: TV" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: TV", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo Handset test" == sel.get_text("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo Handset test"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo Handset test")
        for i in range(60):
            try:
                if "requirement: MeeGo Handset test" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: MeeGo Handset test", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "test cases" == sel.get_text("link=test cases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=test cases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=test cases")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_text_present("del"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("del"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("disconnect"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("disconnect")
        for i in range(60):
            try:
                if sel.is_element_present("save"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("save"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("save")
        for i in range(60):
            try:
                if sel.is_element_present("id_search"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_search"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test6TestcasesAdd(BaseSeleniumTestCase):
    
    def test_6_testcases_add(self):
        sel = self.selenium
        sel.set_timeout("10000")
        sel.open("/require/#requirement/13/details/")
        try: self.failUnless(sel.is_text_present("qualitiorequirements"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "requirement: MeeGo" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if "requirement: TV" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: TV", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo Handset test" == sel.get_text("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo Handset test"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo Handset test")
        for i in range(60):
            try:
                if "requirement: MeeGo Handset test" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: MeeGo Handset test", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "test cases" == sel.get_text("link=test cases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=test cases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=test cases")
        for i in range(60):
            try:
                if sel.is_element_present("id_search"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_search"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_search", "Mee")
        try: self.failUnless(sel.is_element_present("id_search_submit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_search_submit")
        for i in range(60):
            try:
                if sel.is_element_present("connect"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("connect"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=tr td input[value=\"3\"]")
        try: self.failUnless(sel.is_element_present("save"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("save")
        for i in range(60):
            try:
                if sel.is_text_present("TestCase"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("TestCase"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test7ModreqParent(BaseSeleniumTestCase):
    
    def test_7_modreq_parent(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 4")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 4"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 4"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 4")
        sel.click("link=new requirement 4")
        for i in range(60):
            try:
                if "requirement: new requirement 4" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        try: self.failUnless(sel.is_text_present("full name: /MeeGo/TV/new requirement 4"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:path: /MeeGo/TV/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.select("id_parent", "label=/MeeGo/TV/MeeGo Handset test")
        sel.click("css=input.ui-button")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_text_present("requirement: MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo Handset test" == sel.get_text("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo Handset test"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo Handset test")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 4"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=new requirement 4")
        for i in range(60):
            try:
                if "requirement: new requirement 4" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /MeeGo/TV/MeeGo Handset test/new requirement 4"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:requirement: new requirement 4"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("full name: /MeeGo/TV/MeeGo Handset test/new requirement 4"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("exact:path: /MeeGo/TV/MeeGo Handset test/"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test8ModreqReltarg(BaseSeleniumTestCase):
    
    def test_8_modreq_reltarg(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 5")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 5"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 5"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 5")
        sel.click("link=new requirement 5")
	time.sleep(2)
        for i in range(60):
            try:
                if "requirement: new requirement 5" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_release_target"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_release_target"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_release_target")
        sel.click("link=15")
	time.sleep(1)
        sel.click("css=input.ui-button")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 5"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=new requirement 5")
        for i in range(60):
            try:
                if "requirement: new requirement 5" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /MeeGo/TV/new requirement 5"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:requirement: new requirement 5"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=edit")
        for i in range(60):
            try:
                if "" == sel.get_text("id_release_target"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_release_target"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("link=15"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=15"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("15", sel.get_text("link=15"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("15", sel.get_text("css= .ui-state-active"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test9ModreqDesript(BaseSeleniumTestCase):
    
    def test_9_modreq_desript(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 6")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 6"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 6"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 6")
        sel.click("link=new requirement 6")
        for i in range(60):
            try:
                if "requirement: new requirement 6" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_description"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_description", "Desription of test")
        sel.click("css=input.ui-button")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 6"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=new requirement 6")
        for i in range(60):
            try:
                if "requirement: new requirement 6" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /MeeGo/TV/new requirement 6"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:requirement: new requirement 6"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_description"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present(""))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test10ModreqDepend(BaseSeleniumTestCase):
    
    def test_10_modreq_depend(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 7")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 7"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 7"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 7")
        sel.click("link=new requirement 7")
        for i in range(60):
            try:
                if "requirement: new requirement 7" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_dependencies"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_dependencies"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.add_selection("id_dependencies", "label=/MeeGo/IVI")
        sel.click("css=input.ui-button")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 7"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=new requirement 7")
        for i in range(60):
            try:
                if "requirement: new requirement 7" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("full name: /MeeGo/TV/new requirement 7"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:requirement: new requirement 7"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("depends   id path name 3 /MeeGo/ IVI"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("depends   id path name 3 /MeeGo/ IVI"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test11Subrequir(BaseSeleniumTestCase):
    
    def test_11_subrequir(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 8")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 8")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new subrequirement 8")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
	time.sleep(1)
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(1)
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 8")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new sub2requirement 8")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 8")
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: new requirement 8"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("/MeeGo/TV/new requirement 8/"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("new subrequirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("new sub2requirement 8"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test12DetailsVerify(BaseSeleniumTestCase):

    def test_12_details_verify(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        for i in range(60):
            try:
                if sel.is_text_present("MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=div#application-view-header"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("requirement: MeeGo", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("details", sel.get_text("css=div#application-view-menu span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("application-view-menu"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=test cases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div.application-view-content"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("full name: /MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view div.application-view-content div:first-child"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view div.application-view-content div:first-child b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("full name:", sel.get_text("css=div#application-view div.application-view-content div:first-child b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("full name: /MeeGo", sel.get_text("css=div#application-view div.application-view-content div:first-child"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view div.application-view-content div:nth-child(2)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("path: /", sel.get_text("css=div#application-view div.application-view-content div:nth-child(2)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view div.application-view-content div:nth-child(3)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view div.application-view-content h2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("sub-requirements", sel.get_text("css=div#application-view div.application-view-content h2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view div.application-view-content div:nth-child(3)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view div.application-view-content h2:nth-child(1)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("testcases", sel.get_text("css=div#application-view div.application-view-content h2:contains(\"testcases\")"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view-footer div a span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("application-view-footer"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view-footer div"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("new requirement", sel.get_text("css=div#application-view-footer div a span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("depends"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("blocks"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test13EditVerify(BaseSeleniumTestCase):
    
    def test_13_edit_verify(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "requirement: MeeGo" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_text_present("Parent"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("application-view-header"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("application-view-menu"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div.application-view-content"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_release_target")
        try: self.failUnless(sel.is_element_present("parent_wrapper"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_parent"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("name_wrapper"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("release_target_wrapper"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_release_target"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#ui-datepicker-div"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("description_wrapper"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_description"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("dependencies_wrapper"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_dependencies"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("application-view-footer"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("Executed"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=input.ui-button[value='Save']"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test14TestcasesVerify(BaseSeleniumTestCase):
    
    def test_14_testcases_verify(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "requirement: MeeGo" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=test cases")
        for i in range(60):
            try:
                if sel.is_element_present("id_search"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=div#application-view div:nth-child(3)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("search_wrapper"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_search"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id_search_submit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view form div:nth-child(1)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("id"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("path"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=th.path"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=table.available-testcases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=table.pretty"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=div#application-view-footer div"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("save"))
        except AssertionError, e: self.verificationErrors.append(str(e))


if __name__ == "__main__":
    unittest.main()
