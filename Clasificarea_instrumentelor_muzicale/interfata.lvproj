<?xml version='1.0'?>
<Project Type="Project" LVVersion="0">
	<Property Name="NI.LV.All.SaveVersion" Type="Str">24.0</Property>
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Date.lvlib" Type="Library" URL="Date.lvlib">
			<Item Name="Shared_Confidence" Type="Variable">
				<Property Name="varPersistentID" Type="Str">{7924A4F1-6DB3-4768-9D75-6D5420768586}</Property>
			</Item>
			<Item Name="Shared_Instrument" Type="Variable">
				<Property Name="varPersistentID" Type="Str">{40F6144E-8CE6-49C5-B577-1D7478F53DDE}</Property>
			</Item>
		</Item>
		<Item Name="nou" Type="Web Service">
			<Property Name="Bld_buildSpecName" Type="Str"></Property>
			<Property Name="Bld_version.build" Type="Int">7</Property>
			<Property Name="ws.autoIncrementVersion" Type="Bool">true</Property>
			<Property Name="ws.disconnectInline" Type="Bool">true</Property>
			<Property Name="ws.disconnectTypeDefs" Type="Bool">false</Property>
			<Property Name="ws.guid" Type="Str">{3AEB3404-6A49-42DC-AEB1-9126F574E3D6}</Property>
			<Property Name="ws.modifyLibraryFile" Type="Bool">true</Property>
			<Property Name="ws.privilege_role_map_size" Type="Int">0</Property>
			<Property Name="ws.public_folder_name" Type="Str">public</Property>
			<Property Name="ws.remoteDebugging" Type="Bool">false</Property>
			<Property Name="ws.removeLibraryItems" Type="Bool">true</Property>
			<Property Name="ws.removePolyVIs" Type="Bool">true</Property>
			<Property Name="ws.serveDefaultDoc" Type="Bool">true</Property>
			<Property Name="ws.SSE2" Type="Bool">true</Property>
			<Property Name="ws.static_permissions" Type="Str"></Property>
			<Property Name="ws.version.build" Type="Int">7</Property>
			<Property Name="ws.version.fix" Type="Int">0</Property>
			<Property Name="ws.version.major" Type="Int">1</Property>
			<Property Name="ws.version.minor" Type="Int">0</Property>
			<Item Name="Public Content" Type="Folder" URL="public">
				<Property Name="NI.DISK" Type="Bool">true</Property>
			</Item>
			<Item Name="Startup VIs" Type="Startup VIs Container"/>
			<Item Name="Web Resources" Type="HTTP WebResources Container">
				<Item Name="get_data.vi" Type="VI" URL="get_data.vi">
					<Property Name="ws.buffered" Type="Bool">true</Property>
					<Property Name="ws.includeNameInURL" Type="Bool">true</Property>
					<Property Name="ws.keepInMemory" Type="Bool">true</Property>
					<Property Name="ws.loadAtStartup" Type="Bool">true</Property>
					<Property Name="ws.method" Type="Int">1</Property>
					<Property Name="ws.outputFormat" Type="Int">4</Property>
					<Property Name="ws.outputType" Type="Int">0</Property>
					<Property Name="ws.permissions" Type="Str"></Property>
					<Property Name="ws.requireAPIKey" Type="Bool">false</Property>
					<Property Name="ws.requiredPrivilege" Type="Str"></Property>
					<Property Name="ws.type" Type="Int">1</Property>
					<Property Name="ws.uri" Type="Str"></Property>
					<Property Name="ws.useHeaders" Type="Bool">true</Property>
					<Property Name="ws.useStandardURL" Type="Bool">true</Property>
				</Item>
			</Item>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="NI_WebServices.lvlib" Type="Library" URL="/&lt;vilib&gt;/wsapi/NI_WebServices.lvlib">
					<Item Name="compatibility" Type="Folder">
						<Item Name="httpRequestID (LV2012)" Type="Folder">
							<Item Name="subVIs" Type="Folder">
								<Item Name="Get Encrypt Key.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Get Encrypt Key.vi"/>
								<Item Name="Set Boolean ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set Boolean ESP Variable.vi"/>
								<Item Name="Set Double ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set Double ESP Variable.vi"/>
								<Item Name="Set Integer ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set Integer ESP Variable.vi"/>
								<Item Name="Set Many Boolean ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set Many Boolean ESP Variables.vi"/>
								<Item Name="Set Many Double ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set Many Double ESP Variables.vi"/>
								<Item Name="Set Many Integer ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set Many Integer ESP Variables.vi"/>
								<Item Name="Set Many String ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set Many String ESP Variables.vi"/>
								<Item Name="Set String ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Set String ESP Variable.vi"/>
								<Item Name="Write Boolean Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Boolean Session Variable.vi"/>
								<Item Name="Write Double Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Double Session Variable.vi"/>
								<Item Name="Write Integer Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Integer Session Variable.vi"/>
								<Item Name="Write Many Boolean Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Many Boolean Session Variables.vi"/>
								<Item Name="Write Many Double Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Many Double Session Variables.vi"/>
								<Item Name="Write Many Integer Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Many Integer Session Variables.vi"/>
								<Item Name="Write Many Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Many Session Variables.vi"/>
								<Item Name="Write Single Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Write Single Session Variable.vi"/>
							</Item>
							<Item Name="Check If Session Exists.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Check If Session Exists.vi"/>
							<Item Name="Create Session.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Create Session.vi"/>
							<Item Name="Decrypt.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Decrypt.vi"/>
							<Item Name="Delete Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Delete Session Variable.vi"/>
							<Item Name="Destroy Session.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Destroy Session.vi"/>
							<Item Name="Encrypt.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Encrypt.vi"/>
							<Item Name="Flush Output.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Flush Output.vi"/>
							<Item Name="Get Auth Details.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Get Auth Details.vi"/>
							<Item Name="Get Session ID Cookie.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Get Session ID Cookie.vi"/>
							<Item Name="Read All Form Data.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read All Form Data.vi"/>
							<Item Name="Read All Request Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read All Request Variables.vi"/>
							<Item Name="Read All Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read All Session Variables.vi"/>
							<Item Name="Read Form Data.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read Form Data.vi"/>
							<Item Name="Read Postdata.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read Postdata.vi"/>
							<Item Name="Read Request Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read Request Variable.vi"/>
							<Item Name="Read Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read Session Variable.vi"/>
							<Item Name="Read Uploaded Files Info.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read Uploaded Files Info.vi"/>
							<Item Name="Render ESP Template.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Render ESP Template.vi"/>
							<Item Name="Set ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Set ESP Variable.vi"/>
							<Item Name="Set HTTP Header.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Set HTTP Header.vi"/>
							<Item Name="Set HTTP Redirect.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Set HTTP Redirect.vi"/>
							<Item Name="Set HTTP Response Code.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Set HTTP Response Code.vi"/>
							<Item Name="Set HTTP Response MIME Type.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Set HTTP Response MIME Type.vi"/>
							<Item Name="Write Response.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Write Response.vi"/>
							<Item Name="Write Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Write Session Variable.vi"/>
						</Item>
						<Item Name="Read All Form Data (LV2011).vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Read All Form Data (LV2011).vi"/>
					</Item>
					<Item Name="subVIs" Type="Folder">
						<Item Name="Error Converter (ErrCode or Status).vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/subVIs/Error Converter (ErrCode or Status).vi"/>
					</Item>
					<Item Name="Escape HTTP URL.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Escape HTTP URL.vi"/>
					<Item Name="Keyed Array.ctl" Type="VI" URL="/&lt;vilib&gt;/wsapi/Keyed Array.ctl"/>
					<Item Name="LV Image to PNG Data.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/LV Image to PNG Data.vi"/>
					<Item Name="PNG Data to LV Image.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/PNG Data to LV Image.vi"/>
					<Item Name="Unescape HTTP URL.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/VIs/Unescape HTTP URL.vi"/>
					<Item Name="Uploaded Files Array.ctl" Type="VI" URL="/&lt;vilib&gt;/wsapi/Uploaded Files Array.ctl"/>
					<Item Name="Web Request.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/wsapi/Web Request.lvclass">
						<Item Name="Web Request.ctl" Type="Class Private Data" URL="/&lt;vilib&gt;/wsapi/Web Request.lvclass/Web Request.ctl"/>
						<Item Name="subVIs" Type="Folder">
							<Item Name="Get Encrypt Key.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Get Encrypt Key.vi"/>
							<Item Name="Set Boolean ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set Boolean ESP Variable.vi"/>
							<Item Name="Set Double ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set Double ESP Variable.vi"/>
							<Item Name="Set Integer ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set Integer ESP Variable.vi"/>
							<Item Name="Set Many Boolean ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set Many Boolean ESP Variables.vi"/>
							<Item Name="Set Many Double ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set Many Double ESP Variables.vi"/>
							<Item Name="Set Many Integer ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set Many Integer ESP Variables.vi"/>
							<Item Name="Set Many String ESP Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set Many String ESP Variables.vi"/>
							<Item Name="Set String ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Set String ESP Variable.vi"/>
							<Item Name="Write Boolean Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Boolean Session Variable.vi"/>
							<Item Name="Write Double Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Double Session Variable.vi"/>
							<Item Name="Write Integer Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Integer Session Variable.vi"/>
							<Item Name="Write Many Boolean Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Many Boolean Session Variables.vi"/>
							<Item Name="Write Many Double Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Many Double Session Variables.vi"/>
							<Item Name="Write Many Integer Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Many Integer Session Variables.vi"/>
							<Item Name="Write Many Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Many Session Variables.vi"/>
							<Item Name="Write Single Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/subVIs/Write Single Session Variable.vi"/>
						</Item>
						<Item Name="support" Type="Folder">
							<Item Name="Create Web Request.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/support/Create Web Request.vi"/>
							<Item Name="Write httpRequestID.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/support/Write httpRequestID.vi"/>
						</Item>
						<Item Name="Check If Session Exists.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Check If Session Exists.vi"/>
						<Item Name="Create Session.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Create Session.vi"/>
						<Item Name="Decrypt.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Decrypt.vi"/>
						<Item Name="Delete Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Delete Session Variable.vi"/>
						<Item Name="Destroy Session.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Destroy Session.vi"/>
						<Item Name="Encrypt.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Encrypt.vi"/>
						<Item Name="Flush Output.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Flush Output.vi"/>
						<Item Name="Get Auth Details for NI Web Server.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Get Auth Details for NI Web Server.vi"/>
						<Item Name="Get Auth Details.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Get Auth Details.vi"/>
						<Item Name="Get Session ID Cookie.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Get Session ID Cookie.vi"/>
						<Item Name="Read All Form Data.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read All Form Data.vi"/>
						<Item Name="Read All Request Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read All Request Variables.vi"/>
						<Item Name="Read All Session Variables.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read All Session Variables.vi"/>
						<Item Name="Read Form Data.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read Form Data.vi"/>
						<Item Name="Read Postdata.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read Postdata.vi"/>
						<Item Name="Read Request Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read Request Variable.vi"/>
						<Item Name="Read Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read Session Variable.vi"/>
						<Item Name="Read Uploaded Files Info.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read Uploaded Files Info.vi"/>
						<Item Name="Render ESP Template.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Render ESP Template.vi"/>
						<Item Name="Set ESP Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Set ESP Variable.vi"/>
						<Item Name="Set HTTP Header.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Set HTTP Header.vi"/>
						<Item Name="Set HTTP Redirect.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Set HTTP Redirect.vi"/>
						<Item Name="Set HTTP Response Code.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Set HTTP Response Code.vi"/>
						<Item Name="Set HTTP Response MIME Type.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Set HTTP Response MIME Type.vi"/>
						<Item Name="webservices.mnu" Type="Document" URL="/&lt;menus&gt;/Categories/Computer/_webservices/webservices.mnu"/>
						<Item Name="Write Response.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Write Response.vi"/>
						<Item Name="Write Session Variable.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Write Session Variable.vi"/>
					</Item>
					<Item Name="Web Service.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/wsapi/Web Service.lvclass">
						<Item Name="Web Service.ctl" Type="Class Private Data" URL="/&lt;vilib&gt;/wsapi/Web Service.lvclass/Web Service.ctl"/>
						<Item Name="support" Type="Folder">
							<Item Name="Create Web Service.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/support/Create Web Service.vi"/>
							<Item Name="Write wsHandle.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/support/Write wsHandle.vi"/>
						</Item>
						<Item Name="Get Web Service Status.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Get Web Service Status.vi"/>
						<Item Name="Read Service Attribute.vi" Type="VI" URL="/&lt;vilib&gt;/wsapi/class/Read Service Attribute.vi"/>
						<Item Name="webservices-service.mnu" Type="Document" URL="/&lt;menus&gt;/Categories/Computer/_webservices/webservices-service.mnu"/>
					</Item>
				</Item>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib">
					<Item Name="lvfile" Type="Folder">
						<Item Name="Can File be in LLB.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Can File be in LLB.vi"/>
						<Item Name="FT_FileTypes.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/FT_FileTypes.ctl"/>
						<Item Name="Get File Type.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Get File Type.vi"/>
						<Item Name="Get File Type Icon Image.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Get File Type Icon Image.vi"/>
						<Item Name="Is File a LabVIEW document.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Is File a LabVIEW document.vi"/>
						<Item Name="Is File a type of library.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Is File a type of library.vi"/>
						<Item Name="Is File VI.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Is File VI.vi"/>
						<Item Name="Is File an LLB.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Is File an LLB.vi"/>
						<Item Name="LVFileType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/LVFileType.ctl"/>
						<Item Name="Convert filetype to Is VI.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Convert filetype to Is VI.vi"/>
						<Item Name="Convert filetype to Icon Image.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Convert filetype to Icon Image.vi"/>
						<Item Name="Convert filetype to Can be in LLB.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Convert filetype to Can be in LLB.vi"/>
						<Item Name="Convert filetype to Is library type.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Convert filetype to Is library type.vi"/>
						<Item Name="Convert filetype to Is LabVIEW document.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/lvfile.llb/Convert filetype to Is LabVIEW document.vi"/>
					</Item>
				</Item>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
			</Item>
			<Item Name="ws_runtime.dll" Type="Document" URL="ws_runtime.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
