# Surge tvOS

Apple added Network Extension support in tvOS 17, so Surge can now run directly on tvOS. All users who have purchased Surge iOS can use it directly without additional purchases or feature subscriptions.

After upgrading tvOS to 17.0, you can directly install Surge tvOS from the App Store, or use the test version after joining TestFlight, see: [ios-testflight](https://kb.nssurge.com/surge-knowledge-base/faq/ios-testflight "mention").

### Features

The Surge tvOS version uses the same core as the Surge iOS version, that is, all features of Surge iOS can be used in the Surge tvOS version, including scripts, WireGuard and other complex features. However, some features that rely on UI cannot be used, such as traffic statistics.

Also, Surge tvOS can be used as a Surge Ponte server or client. With the correct configuration, Apple TV can be used as a springboard to access the internal network or for remote control of Surge tvOS. For details about Surge Ponte, please refer to [ponte](https://kb.nssurge.com/surge-knowledge-base/guidelines/ponte "mention").

### Getting Started

Please upgrade Surge iOS to version 5.7.0 or above, find the Surge tvOS project on the more page, and then follow the wizard.

Please note that the **main account** logged into Apple TV must be consistent with the **iCloud account** of the Surge iOS device.

### Configuration

Since Surge tvOS cannot access iCloud Drive (tvOS system does not provide this mechanism), all configuration-related operations need to be modified by deploying with Surge iOS.

Please note that since the Surge iOS version cannot evaluate the network situation where Apple TV is located, when configuring the Surge Ponte server, it cannot detect the availability of options like Surge Mac. Please first confirm whether the network or the selected proxy is Full Cone NAT.

#### About External Resources

Different from Surge iOS, Surge tvOS will update external resources for the first time when it starts. At this time, some external strategy groups and external rules may be empty and fall back to DIRECT. Please check the log to confirm whether there are persistent external resources loading failures. If necessary, adjust the rules and strategies to ensure that external resources can be initialized.

You can also view the current remote resource update status through the remote controller and update it manually.

### Control

Surge tvOS does not provide direct UI control functions. All control operations should be completed through Surge iOS. After completing the configuration deployment and starting Surge tvOS, the Apple TV project will automatically appear in the remote controller device list in the tool list. You can control various operations and view requests and statistical results through Surge iOS.

The remote controller accesses through Surge Ponte and can be controlled under any network. If you do not need to use the Surge Ponte penetration function, you can configure Surge Ponte as LAN-Only, only for remote control in the same local area network.

### Debugging

If problems arise during use, press the play button 3 times under the main interface to call out the debug menu. You can view the log in the menu to analyze errors.
