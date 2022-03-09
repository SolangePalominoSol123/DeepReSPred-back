def getTemplateReceivedRequest(idRequest, inputType, inputContent, urlFront):

    html="""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="width:100%;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0"> 
        <head> 
        <meta charset="UTF-8"> 
        <meta content="width=device-width, initial-scale=1" name="viewport"> 
        <meta name="x-apple-disable-message-reformatting"> 
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
        <meta content="telephone=no" name="format-detection"> 
        <title>Request received</title><!--[if (mso 16)]>
            <style type="text/css">
            a {{text-decoration: none;}}
            </style>
            <![endif]--><!--[if gte mso 9]><style>sup {{ font-size: 100% !important; }}</style><![endif]--><!--[if gte mso 9]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG></o:AllowPNG>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]--><!--[if !mso]><!-- --> 
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700,700i" rel="stylesheet"><!--<![endif]--> 
        <style type="text/css">
        #outlook a {{
            padding:0;
        }}
        .ExternalClass {{
            width:100%;
        }}
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {{
            line-height:100%;
        }}
        .es-button {{
            mso-style-priority:100!important;
            text-decoration:none!important;
        }}
        a[x-apple-data-detectors] {{
            color:inherit!important;
            text-decoration:none!important;
            font-size:inherit!important;
            font-family:inherit!important;
            font-weight:inherit!important;
            line-height:inherit!important;
        }}
        .es-desk-hidden {{
            display:none;
            float:left;
            overflow:hidden;
            width:0;
            max-height:0;
            line-height:0;
            mso-hide:all;
        }}
        [data-ogsb] .es-button {{
            border-width:0!important;
            padding:10px 20px 10px 20px!important;
        }}
        [data-ogsb] .es-button.es-button-1 {{
            padding:10px 20px!important;
        }}
        @media only screen and (max-width:600px) {{p, ul li, ol li, a {{ line-height:150%!important }} h1, h2, h3, h1 a, h2 a, h3 a {{ line-height:120%!important }} h1 {{ font-size:30px!important; text-align:center }} h2 {{ font-size:26px!important; text-align:center }} h3 {{ font-size:20px!important; text-align:center }} .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a {{ font-size:30px!important }} .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a {{ font-size:26px!important }} h3 a {{ text-align:center }} .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a {{ font-size:20px!important }} .es-menu td a {{ font-size:16px!important }} .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a {{ font-size:16px!important }} .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a {{ font-size:16px!important }} .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a {{ font-size:16px!important }} .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a {{ font-size:12px!important }} *[class="gmail-fix"] {{ display:none!important }} .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 {{ text-align:center!important }} .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 {{ text-align:right!important }} .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 {{ text-align:left!important }} .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img {{ display:inline!important }} .es-button-border {{ display:block!important }} a.es-button, button.es-button {{ font-size:20px!important; display:block!important; border-width:10px 20px 10px 20px!important }} .es-btn-fw {{ border-width:10px 0px!important; text-align:center!important }} .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right {{ width:100%!important }} .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header {{ width:100%!important; max-width:600px!important }} .es-adapt-td {{ display:block!important; width:100%!important }} .adapt-img {{ width:100%!important; height:auto!important }} .es-m-p0 {{ padding:0!important }} .es-m-p0r {{ padding-right:0!important }} .es-m-p0l {{ padding-left:0!important }} .es-m-p0t {{ padding-top:0!important }} .es-m-p0b {{ padding-bottom:0!important }} .es-m-p20b {{ padding-bottom:20px!important }} .es-mobile-hidden, .es-hidden {{ display:none!important }} tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden {{ width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important }} tr.es-desk-hidden {{ display:table-row!important }} table.es-desk-hidden {{ display:table!important }} td.es-desk-menu-hidden {{ display:table-cell!important }} .es-menu td {{ width:1%!important }} table.es-table-not-adapt, .esd-block-html table {{ width:auto!important }} table.es-social {{ display:inline-block!important }} table.es-social td {{ display:inline-block!important }} .es-m-p5 {{ padding:5px!important }} .es-m-p5t {{ padding-top:5px!important }} .es-m-p5b {{ padding-bottom:5px!important }} .es-m-p5r {{ padding-right:5px!important }} .es-m-p5l {{ padding-left:5px!important }} .es-m-p10 {{ padding:10px!important }} .es-m-p10t {{ padding-top:10px!important }} .es-m-p10b {{ padding-bottom:10px!important }} .es-m-p10r {{ padding-right:10px!important }} .es-m-p10l {{ padding-left:10px!important }} .es-m-p15 {{ padding:15px!important }} .es-m-p15t {{ padding-top:15px!important }} .es-m-p15b {{ padding-bottom:15px!important }} .es-m-p15r {{ padding-right:15px!important }} .es-m-p15l {{ padding-left:15px!important }} .es-m-p20 {{ padding:20px!important }} .es-m-p20t {{ padding-top:20px!important }} .es-m-p20r {{ padding-right:20px!important }} .es-m-p20l {{ padding-left:20px!important }} .es-m-p25 {{ padding:25px!important }} .es-m-p25t {{ padding-top:25px!important }} .es-m-p25b {{ padding-bottom:25px!important }} .es-m-p25r {{ padding-right:25px!important }} .es-m-p25l {{ padding-left:25px!important }} .es-m-p30 {{ padding:30px!important }} .es-m-p30t {{ padding-top:30px!important }} .es-m-p30b {{ padding-bottom:30px!important }} .es-m-p30r {{ padding-right:30px!important }} .es-m-p30l {{ padding-left:30px!important }} .es-m-p35 {{ padding:35px!important }} .es-m-p35t {{ padding-top:35px!important }} .es-m-p35b {{ padding-bottom:35px!important }} .es-m-p35r {{ padding-right:35px!important }} .es-m-p35l {{ padding-left:35px!important }} .es-m-p40 {{ padding:40px!important }} .es-m-p40t {{ padding-top:40px!important }} .es-m-p40b {{ padding-bottom:40px!important }} .es-m-p40r {{ padding-right:40px!important }} .es-m-p40l {{ padding-left:40px!important }} }}
        </style> 
        </head> 
        <body style="width:100%;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0"> 
        <div class="es-wrapper-color" style="background-color:#EFEFEF"><!--[if gte mso 9]>
                    <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                        <v:fill type="tile" color="#efefef"></v:fill>
                    </v:background>
                <![endif]--> 
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top"> 
            <tr style="border-collapse:collapse"> 
            <td valign="top" style="padding:0;Margin:0">  
            <table cellpadding="0" cellspacing="0" class="es-header" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top"> 
                <tr style="border-collapse:collapse"> 
                <td align="center" style="padding:0;Margin:0"> 
                <table class="es-header-body" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#E6EBEF;width:600px"> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" bgcolor="#f8f7f7" style="padding:20px;Margin:0;background-color:#f8f7f7"> 
                    <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td valign="top" align="center" style="padding:0;Margin:0;width:560px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:0;Margin:0;font-size:0px"><a href="{urlFront}" target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#677D9E;font-size:14px"><img src="cid:imageLogo" alt="DeepReSPred" title="DeepReSPred" width="184" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" height="38"></a></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table></td> 
                    </tr> 
                </table></td> 
                </tr> 
            </table> 
            <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
                <tr style="border-collapse:collapse"> 
                <td align="center" style="padding:0;Margin:0"> 
                <table class="es-content-body" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px"> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" background="https://i.ibb.co/rcFjzdD/banner-BUP.png" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:40px;padding-right:40px;background-image:url(https://i.ibb.co/rcFjzdD/banner-BUP.png);background-repeat:no-repeat;background-position:center center"><!--[if mso]><table style="width:520px" cellpadding="0" cellspacing="0"><tr><td style="width:134px" valign="top"><![endif]--> 
                    <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"> 
                        <tr style="border-collapse:collapse"> 
                        <td class="es-m-p0r" valign="top" align="center" style="padding:0;Margin:0;width:134px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:0;Margin:0;display:none"></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td><td style="width:20px"></td><td style="width:366px" valign="top"><![endif]--> 
                    <table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td align="left" style="padding:0;Margin:0;width:366px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" bgcolor="#ffffff" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;background-color:#ffffff;border-radius:12px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="left" style="padding:0;Margin:0;padding-bottom:5px;padding-left:20px;padding-top:30px"><h5 style="Margin:0;line-height:120%;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#341731" class="brand">New Request Information</h5></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-l" align="left" bgcolor="#cabec9" style="padding:0;Margin:0;padding-top:10px;padding-bottom:10px;padding-left:20px"><h3 class="product-name" style="Margin:0;line-height:19px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:19px;font-style:normal;font-weight:normal;color:#682f62">ID Request: {idRequest}</h3></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td align="left" style="Margin:0;padding-top:10px;padding-right:10px;padding-bottom:15px;padding-left:20px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:21px;color:#333333;font-size:14px" class="product-description">DeepReSPred&nbsp;has received successfully your prediction request.</p></td> 
                            </tr>  
                            <tr style="border-collapse:collapse"> 
                            <td align="left" style="padding:0;Margin:0;padding-bottom:5px;padding-right:15px;padding-left:20px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:21px;color:#333333;font-size:14px" class="product-description">You will be able to know the status of the processing or the results of your prediction request just searching your request in our service.</p></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:10px;Margin:0"><span class="es-button-border" style="border-style:solid;border-color:transparent;background:#341731;border-width:0px;display:inline-block;border-radius:4px;width:auto"><a href="{urlFront}{idRequest}" class="es-button es-button-1" target="_blank" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#FFFFFF;font-size:16px;border-style:solid;border-color:#341731;border-width:10px 20px;display:inline-block;background:#341731;border-radius:4px;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;font-weight:normal;font-style:normal;line-height:19px;width:auto;text-align:center">Search request</a></span></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td align="left" style="padding:0;Margin:0;padding-right:10px;padding-left:20px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:12px;color:#333333;font-size:8px" class="product-description"><br></p></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td style="padding:0;Margin:0"> 
                            <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                                <tr style="border-collapse:collapse"> 
                                <td align="center" style="padding:0;Margin:0;display:none"></td> 
                                </tr> 
                            </table></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td></tr></table><![endif]--></td> 
                    </tr> 
                </table>
                </td> 
                </tr> 
            </table> 
            <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
                <tr style="border-collapse:collapse"> 
                <td align="center" style="padding:0;Margin:0"> 
                <table class="es-content-body" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px"> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-top:30px"> 
                    <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td valign="top" align="center" style="padding:0;Margin:0;width:560px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:0;Margin:0"><h2 style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#57276d"><strong>General information</strong></h2></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table></td> 
                    </tr> 
                    <tr style="border-collapse:collapse"> 
                    <td class="esdev-adapt-off" align="left" style="padding:0;Margin:0"> 
                    <table class="esdev-mso-table" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:600px"> 
                        <tr style="border-collapse:collapse"> 
                        <td class="esdev-mso-td" valign="top" style="padding:0;Margin:0"> 
                        <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-p20b" align="left" style="padding:0;Margin:0;width:300px"> 
                            <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                                <tr style="border-collapse:collapse"> 
                                <td align="right" style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0"> 
                                <table width="15%" height="100%" cellspacing="0" cellpadding="0" border="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                                    <tr style="border-collapse:collapse"> 
                                    <td style="padding:0;Margin:0;border-bottom:3px solid #8598b2;background:#FFFFFF none repeat scroll 0% 0%;height:1px;width:100%;margin:0px"></td> 
                                    </tr> 
                                </table></td> 
                                </tr> 
                            </table></td> 
                            </tr> 
                        </table></td> 
                        <td class="esdev-mso-td" valign="top" style="padding:0;Margin:0"> 
                        <table class="es-right" cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="left" style="padding:0;Margin:0;width:300px"> 
                            <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                                <tr style="border-collapse:collapse"> 
                                <td align="left" style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0"> 
                                <table width="15%" height="100%" cellspacing="0" cellpadding="0" border="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                                    <tr style="border-collapse:collapse"> 
                                    <td style="padding:0;Margin:0;border-bottom:3px solid #57276d;background:none 0% 0% repeat scroll #FFFFFF;height:1px;width:100%;margin:0px"></td> 
                                    </tr> 
                                </table></td> 
                                </tr> 
                            </table></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table></td> 
                    </tr> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" style="padding:0;Margin:0;padding-top:10px;padding-left:20px;padding-right:20px"> 
                    <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td valign="top" align="center" style="padding:0;Margin:0;width:560px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:21px;color:#333333;font-size:14px">We have received this data input&nbsp;to perform the prediction process:</p></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table></td> 
                    </tr> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" style="padding:0;Margin:0;padding-top:20px;padding-right:20px;padding-left:40px"><!--[if mso]><table style="width:540px" cellpadding="0"
                                    cellspacing="0"><tr><td style="width:30px" valign="top"><![endif]--> 
                    <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"> 
                        <tr style="border-collapse:collapse"> 
                        <td class="es-m-p0r es-m-p20b" valign="top" align="center" style="padding:0;Margin:0;width:30px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;font-size:0px"><img src="cid:imageGrain" alt="icon" title="icon" width="30" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;font-size:12px" height="30"></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td><td style="width:25px"></td><td style="width:485px" valign="top"><![endif]--> 
                    <table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td align="left" style="padding:0;Margin:0;width:485px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-c" esdev-links-color="#3e8eb8" align="left" style="padding:0;Margin:0;padding-bottom:5px"><h3 style="Margin:0;line-height:23px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:19px;font-style:normal;font-weight:normal;color:#333333"><a target="_blank" href="" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;text-align:center;color:#341731;font-size:19px">Input type</a></h3></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-c" align="left" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:21px;color:#333333;font-size:14px">{inputType}</p></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td></tr></table><![endif]--></td> 
                    </tr> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" style="padding:0;Margin:0;padding-top:20px;padding-right:20px;padding-left:40px"><!--[if mso]><table style="width:540px" cellpadding="0"
                                    cellspacing="0"><tr><td style="width:30px" valign="top"><![endif]--> 
                    <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"> 
                        <tr style="border-collapse:collapse"> 
                        <td class="es-m-p0r es-m-p20b" valign="top" align="center" style="padding:0;Margin:0;width:30px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;font-size:0px"><img src="cid:imageGrain" alt="icon" title="icon" width="30" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;font-size:12px" height="30"></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td><td style="width:25px"></td><td style="width:485px" valign="top"><![endif]--> 
                    <table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td align="left" style="padding:0;Margin:0;width:485px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-c" esdev-links-color="#3e8eb8" align="left" style="padding:0;Margin:0;padding-bottom:5px"><h3 style="Margin:0;line-height:23px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:19px;font-style:normal;font-weight:normal;color:#333333"><a target="_blank" href="" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;text-align:center;color:#341731;font-size:19px">Input content</a></h3></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-c" align="left" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:21px;color:#333333;font-size:14px">{inputContent}</p></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td></tr></table><![endif]--></td> 
                    </tr> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" style="Margin:0;padding-bottom:20px;padding-left:20px;padding-right:20px;padding-top:30px"> 
                    <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td valign="top" align="center" style="padding:0;Margin:0;width:560px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:21px;color:#333333;font-size:14px">Your prediction request results will also be sent by email just finished the process. This process could last some minutes or hours depending on the repeat family size or the sequence length.</p></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table></td> 
                    </tr> 
                </table></td> 
                </tr> 
            </table> 
            <table cellpadding="0" cellspacing="0" class="es-footer" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top"> 
                <tr style="border-collapse:collapse"> 
                <td align="center" style="padding:0;Margin:0"> 
                <table class="es-footer-body" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#E6EBEF;width:600px"> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" bgcolor="#cabec9" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:#cabec9"> 
                    <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td valign="top" align="center" style="padding:0;Margin:0;width:560px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:0;Margin:0;padding-top:10px;padding-left:15px;padding-right:15px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:21px;color:#333333;font-size:14px">DeepReSPred is part of an Informatic Engineer Investigation Project from</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:30px;color:#333333;font-size:20px">Pontificia&nbsp;Universidad Católica del Perú</p></td> 
                            </tr> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="Margin:0;padding-bottom:10px;padding-top:15px;padding-left:15px;padding-right:15px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:17px;color:#333333;font-size:11px">You are receiving this email because you have visited our site and send a request.</p></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table></td> 
                    </tr> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" bgcolor="#efefef" style="padding:20px;Margin:0;background-color:#efefef"><!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:192px" valign="top"><![endif]--> 
                    <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"> 
                        <tr style="border-collapse:collapse"> 
                        <td class="es-m-p20b" align="center" style="padding:0;Margin:0;width:187px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td class="es-m-txt-l" align="left" style="padding:0;Margin:0;font-size:0px"><a target="_blank" href="{urlFront}" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#2E3951;font-size:13px"><img src="cid:imageLogo" alt="DeepReSPred" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="168" title="DeepReSPred" height="35"></a></td> 
                            </tr> 
                        </table></td> 
                        <td class="es-hidden" style="padding:0;Margin:0;width:5px"></td> 
                        </tr> 
                    </table><!--[if mso]></td><td style="width:161px" valign="top"><![endif]--> 
                    <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"> 
                        <tr style="border-collapse:collapse"> 
                        <td class="es-m-p20b" align="left" style="padding:0;Margin:0;width:161px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td valign="top" align="right" style="padding:0;Margin:0;padding-right:10px;width:30px"><img src="cid:imageTelf" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="26" height="26"></td> 
                            <td align="left" style="padding:0;Margin:0"> 
                            <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                                <tr style="border-collapse:collapse"> 
                                <td align="left" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:20px;color:#333333;font-size:13px">+51 967770360</p></td> 
                                </tr> 
                            </table></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td><td style="width:5px"></td><td style="width:202px" valign="top"><![endif]--> 
                    <table class="es-right" cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right"> 
                        <tr style="border-collapse:collapse"> 
                        <td align="left" style="padding:0;Margin:0;width:202px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td valign="top" align="right" style="padding:0;Margin:0;padding-right:10px;width:30px;font-size:0px"><img src="cid:imageMail" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="26" height="26"></td> 
                            <td align="left" style="padding:0;Margin:0"> 
                            <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                                <tr style="border-collapse:collapse"> 
                                <td align="left" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:20px;color:#333333;font-size:13px">deeprespred@gmail.com</p></td> 
                                </tr> 
                            </table></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table><!--[if mso]></td></tr></table><![endif]--></td> 
                    </tr> 
                </table></td> 
                </tr> 
            </table> 
            <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
                <tr style="border-collapse:collapse"> 
                <td align="center" style="padding:0;Margin:0"> 
                <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px" cellspacing="0" cellpadding="0" align="center"> 
                    <tr style="border-collapse:collapse"> 
                    <td align="left" style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px"> 
                    <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                        <tr style="border-collapse:collapse"> 
                        <td valign="top" align="center" style="padding:0;Margin:0;width:560px"> 
                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                            <tr style="border-collapse:collapse"> 
                            <td align="center" style="padding:0;Margin:0;display:none"></td> 
                            </tr> 
                        </table></td> 
                        </tr> 
                    </table></td> 
                    </tr> 
                </table></td> 
                </tr> 
            </table></td> 
            </tr> 
        </table> 
        </div>  
        </body>
        </html>
    """.format(idRequest=idRequest, inputType=inputType, inputContent=inputContent, urlFront=urlFront)
    
    return html