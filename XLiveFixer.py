# -----------------------------------------------------------------------
# kiwidog

import idaapi
import idautils
from idaapi import PluginForm
from PySide import QtGui, QtCore
xlive_dict = { 'xlive_1': '_TitleExports_XWSAStartup@8',
'xlive_2': '_TitleExports_XWSACleanup@0',
'xlive_3': '_TitleExports_XSocketCreate@12',
'xlive_4': '_TitleExports_XSocketClose@4',
'xlive_5': '_TitleExports_XSocketShutdown@8',
'xlive_6': '_TitleExports_XSocketIOCTLSocket@12',
'xlive_7': '_TitleExports_XSocketSetSockOpt@20',
'xlive_8': '_TitleExports_XSocketGetSockOpt@20',
'xlive_9': '_TitleExports_XSocketGetSockName@12',
'xlive_10': '_TitleExports_XSocketGetPeerName@12',
'xlive_11': '_TitleExports_XSocketBind@12',
'xlive_12': '_TitleExports_XSocketConnect@12',
'xlive_13': '_TitleExports_XSocketListen@8',
'xlive_14': '_TitleExports_XSocketAccept@12',
'xlive_15': '_TitleExports_XSocketSelect@20',
'xlive_16': '_TitleExports_XWSAGetOverlappedResult@20',
'xlive_17': '_TitleExports_XWSACancelOverlappedIO@4',
'xlive_18': '_TitleExports_XSocketRecv@16',
'xlive_19': '_TitleExports_XWSARecv@28',
'xlive_20': '_TitleExports_XSocketRecvFrom@24',
'xlive_21': '_TitleExports_XWSARecvFrom@36',
'xlive_22': '_TitleExports_XSocketSend@16',
'xlive_23': '_TitleExports_XWSASend@28',
'xlive_24': '_TitleExports_XSocketSendTo@24',
'xlive_25': '_TitleExports_XWSASendTo@36',
'xlive_26': '_TitleExports_XSocketInet_Addr@4',
'xlive_27': '_TitleExports_XWSAGetLastError@0',
'xlive_28': '_TitleExports_XWSASetLastError@4',
'xlive_29': '_TitleExports_XWSACreateEvent@0',
'xlive_30': '_TitleExports_XWSACloseEvent@4',
'xlive_31': '_TitleExports_XWSASetEvent@4',
'xlive_32': '_TitleExports_XWSAResetEvent@4',
'xlive_33': '_TitleExports_XWSAWaitForMultipleEvents@20',
'xlive_34': '_TitleExports___XWSAFDIsSet@8',
'xlive_35': '_TitleExports_XWSAEventSelect@12',
'xlive_37': '_TitleExports_XSocketHTONL@4',
'xlive_38': '_TitleExports_XSocketNTOHS@4',
'xlive_39': '_TitleExports_XSocketHTONL@4_2',
'xlive_40': '_TitleExports_XSocketNTOHS@4_2',
'xlive_51': '_TitleExports_XNetStartup@4',
'xlive_52': '_TitleExports_XNetCleanup@0',
'xlive_53': '_TitleExports_XNetRandom@8',
'xlive_54': '_TitleExports_XNetCreateKey@8',
'xlive_55': '_TitleExports_XNetRegisterKey@8',
'xlive_56': '_TitleExports_XNetUnregisterKey@4',
'xlive_57': '_TitleExports_XNetXnAddrToInAddr@12',
'xlive_58': '_TitleExports_XNetServerToInAddr@12',
'xlive_60': '_TitleExports_XNetInAddrToXnAddr@12',
'xlive_62': '_TitleExports_XNetInAddrToString@12',
'xlive_63': '_TitleExports_XNetUnregisterInAddr@4',
'xlive_64': '_TitleExports_XNetXnAddrToMachineId@8',
'xlive_65': '_TitleExports_XNetConnect@4',
'xlive_66': '_TitleExports_XNetGetConnectStatus@4',
'xlive_67': '_TitleExports_XNetDnsLookup@12',
'xlive_68': '_TitleExports_XNetDnsRelease@4',
'xlive_69': '_TitleExports_XNetQosListen@20',
'xlive_70': '_TitleExports_XNetQosLookup@48',
'xlive_71': '_TitleExports_XNetQosServiceLookup@12',
'xlive_72': '_TitleExports_XNetQosRelease@4',
'xlive_73': '_TitleExports_XNetGetTitleXnAddr@4',
'xlive_75': '_TitleExports_XNetGetEthernetLinkStatus@0',
'xlive_76': '_TitleExports_XNetGetBroadcastVersionStatus@4',
'xlive_77': '_TitleExports_XNetQosGetListenStats@8',
'xlive_78': '_TitleExports_XNetGetOpt@12',
'xlive_79': '_TitleExports_XNetSetOpt@12',
'xlive_81': '_TitleExports_XNetReplaceKey@8',
'xlive_82': '_TitleExports_XNetGetXnAddrPlatform@8',
'xlive_83': '_TitleExports_XNetGetSystemLinkPort@4',
'xlive_84': '_TitleExports_XNetSetSystemLinkPort@4',
'xlive_472': '_XCustomSetAction@12',
'xlive_473': '_XCustomGetLastActionPress@12',
'xlive_474': '_XCustomSetDynamicActions@20',
'xlive_476': '_XCustomGetLastActionPressEx@20',
'xlive_477': '_XCustomRegisterDynamicActions@0',
'xlive_478': '_XCustomUnregisterDynamicActions@0',
'xlive_479': '_XCustomGetCurrentGamercard@8',
'xlive_651': '_XNotifyGetNext@16',
'xlive_652': '_XNotifyPositionUI@4',
'xlive_653': '_XNotifyDelayUI@4',
'xlive_1082': '_XGetOverlappedExtendedError@4',
'xlive_1083': '_XGetOverlappedResult@12',
'xlive_5000': '?XLiveInitialize@@YGJPAU_XLIVE_INITIALIZE_INFO@@@Z',
'xlive_5001': '_XLiveInput@4',
'xlive_5002': '_XLiveRender@0',
'xlive_5003': '_XLiveUnInitialize@0',
'xlive_5005': '_XLiveOnCreateDevice@8',
'xlive_5006': '_XLiveOnDestroyDevice@0',
'xlive_5007': '_XLiveOnResetDevice@4',
'xlive_5008': '_XHVCreateEngine@12',
'xlive_5010': '_XLiveRegisterDataSection@12',
'xlive_5011': '_XLiveUnregisterDataSection@4',
'xlive_5012': '_XLiveUpdateHashes@8',
'xlive_5016': '_XLivePBufferAllocate@8',
'xlive_5017': '_XLivePBufferFree@4',
'xlive_5018': '_XLivePBufferGetByte@12',
'xlive_5019': '_XLivePBufferSetByte@12',
'xlive_5020': '_XLivePBufferGetDWORD@12',
'xlive_5021': '_XLivePBufferSetDWORD@12',
'xlive_5022': '_XLiveGetUpdateInformation@4',
'xlive_5023': '_XNetGetCurrentAdapter@8',
'xlive_5024': '_XLiveUpdateSystem@4',
'xlive_5025': '_XLiveGetLiveIdError@16',
'xlive_5026': '_XLiveSetSponsorToken@8',
'xlive_5027': '_XLiveUninstallTitle@4',
'xlive_5028': '_XLiveLoadLibraryEx@12',
'xlive_5029': '_XLiveFreeLibrary@4',
'xlive_5030': '_XLivePreTranslateMessage@4',
'xlive_5031': '_XLiveSetDebugLevel@8',
'xlive_5032': '_XLiveVerifyArcadeLicense@8',
'xlive_5034': '_XLiveProtectData@20',
'xlive_5035': '_XLiveUnprotectData@20',
'xlive_5036': '_XLiveCreateProtectedDataContext@8',
'xlive_5037': '_XLiveQueryProtectedDataInformation@8',
'xlive_5038': '_XLiveCloseProtectedDataContext@4',
'xlive_5039': '_XLiveVerifyDataFile@4',
'xlive_5206': '_XShowMessagesUI@4',
'xlive_5208': '_XShowGameInviteUI@16',
'xlive_5209': '_XShowMessageComposeUI@16',
'xlive_5210': '_XShowFriendRequestUI@12',
'xlive_5212': '_XShowCustomPlayerListUI@48',
'xlive_5214': '_XShowPlayerReviewUI@12',
'xlive_5215': '_XShowGuideUI@4',
'xlive_5216': '_XShowKeyboardUI@32',
'xlive_5218': '_XShowArcadeUI@4',
'xlive_5230': '_XLocatorServerAdvertise@60',
'xlive_5231': '_XLocatorServerUnAdvertise@8',
'xlive_5233': '_XLocatorGetServiceProperty@16',
'xlive_5234': '_XLocatorCreateServerEnumerator@40',
'xlive_5235': '_XLocatorCreateServerEnumeratorByIDs@32',
'xlive_5236': '_XLocatorServiceInitialize@8',
'xlive_5237': '_XLocatorServiceUnInitialize@4',
'xlive_5238': '_XLocatorCreateKey@8',
'xlive_5250': '_XShowAchievementsUI@4',
'xlive_5251': '_XCloseHandle@4',
'xlive_5252': '_XShowGamerCardUI@12',
'xlive_5254': '_XCancelOverlapped@4',
'xlive_5255': '_XEnumerateBack@20',
'xlive_5256': '_XEnumerate@20',
'xlive_5257': '_XLiveManageCredentials@16',
'xlive_5258': '_XLiveSignout@4',
'xlive_5259': '_XLiveSignin@16',
'xlive_5260': '_XShowSigninUI@8',
'xlive_5261': '_XUserGetXUID@8',
'xlive_5262': '_XUserGetSigninState@4',
'xlive_5263': '_XUserGetName@12',
'xlive_5264': '_XUserAreUsersFriends@20',
'xlive_5265': '_XUserCheckPrivilege@12',
'xlive_5266': '_XShowMessageBoxUI@36',
'xlive_5267': '_XUserGetSigninInfo@12',
'xlive_5270': '_XNotifyCreateListener@8',
'xlive_5271': '_XShowPlayersUI@4',
'xlive_5273': '_XUserReadGamerPictureByKey@24',
'xlive_5274': '_XUserAwardGamerPicture@16',
'xlive_5275': '_XShowFriendsUI@4',
'xlive_5276': '_XUserSetProperty@16',
'xlive_5277': '_XUserSetContext@12',
'xlive_5278': '_XUserWriteAchievements@12',
'xlive_5279': '_XUserReadAchievementPicture@28',
'xlive_5280': '_XUserCreateAchievementEnumerator@36',
'xlive_5281': '_XUserReadStats@32',
'xlive_5282': '_XUserReadGamerPicture@24',
'xlive_5284': '_XUserCreateStatsEnumeratorByRank@28',
'xlive_5285': '_XUserCreateStatsEnumeratorByRating@32',
'xlive_5286': '_XUserCreateStatsEnumeratorByXuid@32',
'xlive_5287': '_XUserResetStatsView@12',
'xlive_5288': '_XUserGetProperty@16',
'xlive_5289': '_XUserGetContext@12',
'xlive_5290': '_XUserGetReputationStars@4',
'xlive_5291': '_XUserResetStatsViewAllUsers@8',
'xlive_5292': '_XUserSetContextEx@16',
'xlive_5293': '_XUserSetPropertyEx@20',
'xlive_5294': '_XLivePBufferGetByteArray@16',
'xlive_5295': '_XLivePBufferSetByteArray@16',
'xlive_5296': '_XLiveGetLocalOnlinePort@4',
'xlive_5297': '_XLiveInitializeEx@8',
'xlive_5298': '_XLiveGetGuideKey@4',
'xlive_5299': '_XShowGuideKeyRemapUI@4',
'xlive_5300': '_TitleExport_XSessionCreate@32',
'xlive_5303': '_TitleExport_XStringVerify@28',
'xlive_5304': '_TitleExport_XStorageUploadFromMemoryGetProgress@16',
'xlive_5305': '_TitleExport_XStorageUploadFromMemory@20',
'xlive_5306': '_TitleExport_XStorageEnumerate@28',
'xlive_5307': '_TitleExport_XStorageDownloadToMemoryGetProgress@16',
'xlive_5308': '_TitleExport_XStorageDelete@12',
'xlive_5309': '_TitleExport_XStorageBuildServerPathByXuid@32',
'xlive_5310': '_TitleExport_XOnlineStartup@0',
'xlive_5311': '_TitleExport_XOnlineCleanup@0',
'xlive_5312': '_TitleExport_XFriendsCreateEnumerator@20',
'xlive_5313': '_TitleExport_XPresenceInitialize@4',
'xlive_5314': '_XUserMuteListQuery@16',
'xlive_5315': '_TitleExport_XInviteGetAcceptedInfo@8',
'xlive_5316': '_TitleExport_XInviteSend@20',
'xlive_5317': '_TitleExport_XSessionWriteStats@24',
'xlive_5318': '_TitleExport_XSessionStart@12',
'xlive_5319': '_TitleExport_XSessionSearchEx@44',
'xlive_5320': '_TitleExport_XSessionSearchByID@24',
'xlive_5321': '_TitleExport_XSessionSearch@40',
'xlive_5322': '_TitleExport_XSessionModify@20',
'xlive_5323': '_TitleExport_XSessionMigrateHost@16',
'xlive_5324': '_TitleExport_XOnlineGetNatType@0',
'xlive_5325': '_TitleExport_XSessionLeaveLocal@16',
'xlive_5326': '_TitleExport_XSessionJoinRemote@20',
'xlive_5327': '_TitleExport_XSessionJoinLocal@20',
'xlive_5328': '_TitleExport_XSessionGetDetails@16',
'xlive_5329': '_TitleExport_XSessionFlushStats@8',
'xlive_5330': '_TitleExport_XSessionDelete@8',
'xlive_5331': '_TitleExport_XUserReadProfileSettings@28',
'xlive_5332': '_TitleExport_XSessionEnd@8',
'xlive_5333': '_TitleExport_XSessionArbitrationRegister@28',
'xlive_5334': '_XOnlineGetServiceInfo@8',
'xlive_5335': '_XTitleServerCreateEnumerator@16',
'xlive_5336': '_TitleExport_XSessionLeaveRemote@16',
'xlive_5337': '_TitleExport_XUserWriteProfileSettings@16',
'xlive_5338': '_TitleExport_XPresenceSubscribe@12',
'xlive_5339': '_TitleExport_XUserReadProfileSettingsByXuid@36',
'xlive_5340': '_TitleExport_XPresenceCreateEnumerator@28',
'xlive_5341': '_TitleExport_XPresenceUnsubscribe@12',
'xlive_5342': '_TitleExport_XSessionModifySkill@16',
'xlive_5343': '_TitleExport_XSessionCalculateSkill@20',
'xlive_5344': '_TitleExport_XStorageBuildServerPath@28',
'xlive_5345': '_TitleExport_XStorageDownloadToMemory@28',
'xlive_5346': '_TitleExport_XUserEstimateRankForRating@20',
'xlive_5347': '_XLiveProtectedLoadLibrary@20',
'xlive_5348': '_XLiveProtectedCreateFile@36',
'xlive_5349': '_XLiveProtectedVerifyFile@12',
'xlive_5350': '_XLiveContentCreateAccessHandle@28',
'xlive_5351': '_XLiveContentInstallPackage@12',
'xlive_5352': '_XLiveContentUninstall@12',
'xlive_5354': '_XLiveContentVerifyInstalledPackage@8',
'xlive_5355': '_XLiveContentGetPath@16',
'xlive_5356': '_XLiveContentGetDisplayName@16',
'xlive_5357': '_XLiveContentGetThumbnail@16',
'xlive_5358': '_XLiveContentInstallLicense@12',
'xlive_5359': '_XLiveGetUPnPState@4',
'xlive_5360': '_XLiveContentCreateEnumerator@16',
'xlive_5361': '_XLiveContentRetrieveOffersByDate@24',
'xlive_5362': '_XLiveMarketplaceDoesContentIdMatch@8',
'xlive_5363': '_XLiveContentGetLicensePath@16',
'xlive_5365': '_XShowMarketplaceUI@20',
'xlive_5366': '_XShowMarketplaceDownloadItemsUI@24',
'xlive_5367': '_TitleExport_XContentGetMarketplaceCounts@20',
'xlive_5370': '_TitleExport_XMarketplaceConsumeAssets@16',
'xlive_5371': '_XMarketplaceCreateAssetEnumerator@16',
'xlive_5372': '_XMarketplaceCreateOfferEnumerator@24',
'xlive_5374': '_XMarketplaceGetDownloadStatus@16',
'xlive_5375': '_XMarketplaceGetImageUrl@20',
'xlive_5376': '_XMarketplaceCreateOfferEnumeratorByOffering@24',
'xlive_5377': '_TitleExport_XUserFindUsers@28' }
# --------------------------------------------------------------------------
class XLiveImportFixer_t():
    def imports_names_cb(self, ea, name, ord):
        self.items.append((ea, '' if not name else name, ord))
        # True -> Continue enumeration
        return True

    def BuildImports(self):
        print "BuildImports"
        tree = {}
        nimps = idaapi.get_import_module_qty()
        for i in xrange(0, nimps):
            name = idaapi.get_import_module_name(i)
            if not name:
                continue
            # Create a list for imported names
            self.items = []
            # Enum imported entries in this module
            idaapi.enum_import_names(i, self.imports_names_cb)
            if name not in tree:
                tree[name] = []
            tree[name].extend(self.items)
        return tree

    def BuildExports(self):
        return list(idautils.Entries())

    # def PopulateImports(self):
        # print "Populate Imports"
        # for dll_name, imp_entries in self.BuildImports().items():
            # for imp_ea, imp_name, imp_ord in imp_entries:
                # if imp_name.startswith("xlive"):
                    # print imp_ord, imp_ea, imp_name, GetFunctionName(imp_ea)

    # def PopulateExports(self):
        # # Build exports
        # print "Populate Exports"
        # for exp_i, exp_ord, exp_ea, exp_name in self.BuildExports():
            # print "'{}': '{}',".format(exp_name, GetFunctionName(exp_ea)) #print exp_ord, exp_ea, exp_name, GetFunctionName(exp_ea)

			
    def FixImports(self):
        global xlive_dict
        self.dict = xlive_dict
        print "Fixing Imports"
        for dll_name, imp_entries in self.BuildImports().items():
            for imp_ea, imp_name, imp_ord in imp_entries:
                
                if imp_name.startswith("__imp_xlive"):
                    # print imp_ord
                    for xref in XrefsTo(imp_ea, 0):
                        MakeNameEx(xref.frm, self.dict['xlive_' + str(imp_ord)], idaapi.SN_NOWARN)
                        print "Setting {} to {}".format(xref.frm, self.dict['xlive_' + str(imp_ord)])
                    #print "Setting {} to {}".format(imp_ea, self.dict[imp_name[11:]])
                    MakeName(imp_ea, "__jmp_" + self.dict['xlive_' + str(imp_ord)])
                if imp_name.startswith("xlive"):
                    print "Setting {} to {}".format(imp_ea, self.dict['xlive_' + str(imp_ord)])
                    MakeNameEx(imp_ea, self.dict['xlive_' + str(imp_ord)], idaapi.SN_NOWARN)#print imp_ord, imp_ea, imp_name, GetFunctionName(imp_ea)
    def FixExports(self):
        global xlive_dict
        self.dict = xlive_dict
        print "Fixing Exports"
        for exp_i, exp_ord, exp_ea, exp_name in self.BuildExports():
            if exp_name.startswith("xlive"):
                print "Setting {} to {}".format(exp_ea, self.dict['xlive_' + str(imp_ord)])
                MakeName(exp_ea, self.dict['xlive_' + str(imp_ord)])
                
    def Populate(self):
        self.FixImports()
        self.FixExports()
        # self.PopulateImports()
        # self.PopulateExports()
# --------------------------------------------------------------------------
def main():
    print "Main"
    global XLiveImportFixer
    global ordinalDict
	
    XLiveImportFixer_t().Populate()
# --------------------------------------------------------------------------
main()
