
The root workunit folder can contain folder links. If you, for instance, want to link to the samples folder, you just create a link: mklink /d [linkName] [targetPath].
The linkName can be anything except System or Custom and the targetPath points to the folder where the workunits are stored. TargetPath must be fully qualified!

For instance:
mklink /d samples C:\TFS\Dev\Titatinum\Branch3\Samples\BL\WorkUnits

-------------
Standard categories for workunit jobs (Supported in SP8 update2 and newer)

The job node can have a category for specifyiyng where the job can execute like this sample:
<job category="AnyServer"....

AnyServer - Will be executed on one random server in the interval specified by the queue. This is the default and will be used when category is not specified.

AllServers - Will be executed on all the servers in the interval specified by the queue.

SecureZone - Will be executed on one of the servers in secured zone.

InternalZone - Will be executed on one server outside secured zone (internal zone or any of the servers if secured zone are not installed)

InternalAndSecureZone - Will be executed on one server in secured zone AND one server outside secured zone (internal zone or any of the servers if secured zone are not installed)

SecureZoneOrSecureFileArchive - will be executed if the server is in secure zone or if it has the "Secure file archive behind firewall" configuration.

Server:<name> - Will be executed only on the server with the specified name. If you want a job to execute on a server called MyServer you can specify it like this in the .wu file:
<job category="Server:MyServer"....

For more documentation see community


----------------------------------------------------

Test folder is for workflows that test the standard system