# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class EsimProfileList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the EsimProfileList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileList
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileList
        """
        super(EsimProfileList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/ESimProfiles'.format(**self._solution)

    def create(self, callback_url=values.unset, callback_method=values.unset,
               generate_matching_id=values.unset, eid=values.unset):
        """
        Create the EsimProfileInstance

        :param unicode callback_url: The URL we should call after we have sent when the status of the eSIM Profile changes
        :param unicode callback_method: The HTTP method we should use to call callback_url
        :param bool generate_matching_id: When set to `true`, generates a matching ID that identifies the specific eSIM profile that can be downloaded
        :param unicode eid: Identifier of the eUICC that will claim the eSIM Profile

        :returns: The created EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        data = values.of({
            'CallbackUrl': callback_url,
            'CallbackMethod': callback_method,
            'GenerateMatchingId': generate_matching_id,
            'Eid': eid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return EsimProfileInstance(self._version, payload, )

    def stream(self, eid=values.unset, sim_sid=values.unset, status=values.unset,
               limit=None, page_size=None):
        """
        Streams EsimProfileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode eid: List the eSIM Profiles that have been associated with an EId
        :param unicode sim_sid: Find the eSIM Profile resource related to a Sim resource by providing the SIM SID
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.esim_profile.EsimProfileInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(eid=eid, sim_sid=sim_sid, status=status, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, eid=values.unset, sim_sid=values.unset, status=values.unset,
             limit=None, page_size=None):
        """
        Lists EsimProfileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode eid: List the eSIM Profiles that have been associated with an EId
        :param unicode sim_sid: Find the eSIM Profile resource related to a Sim resource by providing the SIM SID
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.esim_profile.EsimProfileInstance]
        """
        return list(self.stream(eid=eid, sim_sid=sim_sid, status=status, limit=limit, page_size=page_size, ))

    def page(self, eid=values.unset, sim_sid=values.unset, status=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param unicode eid: List the eSIM Profiles that have been associated with an EId
        :param unicode sim_sid: Find the eSIM Profile resource related to a Sim resource by providing the SIM SID
        :param EsimProfileInstance.Status status: List the eSIM Profiles that are in a given status
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        """
        data = values.of({
            'Eid': eid,
            'SimSid': sim_sid,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return EsimProfilePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return EsimProfilePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a EsimProfileContext

        :param sid: The SID of the eSIM Profile resource to fetch

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        return EsimProfileContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a EsimProfileContext

        :param sid: The SID of the eSIM Profile resource to fetch

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        return EsimProfileContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.EsimProfileList>'


class EsimProfilePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the EsimProfilePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfilePage
        """
        super(EsimProfilePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EsimProfileInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        return EsimProfileInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.EsimProfilePage>'


class EsimProfileContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sid):
        """
        Initialize the EsimProfileContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the eSIM Profile resource to fetch

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        super(EsimProfileContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/ESimProfiles/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the EsimProfileInstance

        :returns: The fetched EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EsimProfileInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.EsimProfileContext {}>'.format(context)


class EsimProfileInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Status(object):
        NEW = "new"
        RESERVING = "reserving"
        AVAILABLE = "available"
        DOWNLOADED = "downloaded"
        INSTALLED = "installed"
        FAILED = "failed"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the EsimProfileInstance

        :returns: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        super(EsimProfileInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'iccid': payload.get('iccid'),
            'sim_sid': payload.get('sim_sid'),
            'status': payload.get('status'),
            'eid': payload.get('eid'),
            'smdp_plus_address': payload.get('smdp_plus_address'),
            'matching_id': payload.get('matching_id'),
            'activation_code': payload.get('activation_code'),
            'error_code': payload.get('error_code'),
            'error_message': payload.get('error_message'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: EsimProfileContext for this EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileContext
        """
        if self._context is None:
            self._context = EsimProfileContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account to which the eSIM Profile resource belongs
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def iccid(self):
        """
        :returns: The ICCID associated with the Sim resource
        :rtype: unicode
        """
        return self._properties['iccid']

    @property
    def sim_sid(self):
        """
        :returns: The SID of the Sim resource that this eSIM Profile controls
        :rtype: unicode
        """
        return self._properties['sim_sid']

    @property
    def status(self):
        """
        :returns: The status of the eSIM Profile
        :rtype: EsimProfileInstance.Status
        """
        return self._properties['status']

    @property
    def eid(self):
        """
        :returns: Identifier of the eUICC that can claim the eSIM Profile
        :rtype: unicode
        """
        return self._properties['eid']

    @property
    def smdp_plus_address(self):
        """
        :returns: Address of the SM-DP+ server from which the Profile will be downloaded
        :rtype: unicode
        """
        return self._properties['smdp_plus_address']

    @property
    def matching_id(self):
        """
        :returns: Unique identifier of the eSIM profile that be used to identify and download the eSIM profile
        :rtype: unicode
        """
        return self._properties['matching_id']

    @property
    def activation_code(self):
        """
        :returns: Combined machine-readable activation code for acquiring an eSIM Profile with the Activation Code download method
        :rtype: unicode
        """
        return self._properties['activation_code']

    @property
    def error_code(self):
        """
        :returns: Code indicating the failure if the download of the SIM Profile failed and the eSIM Profile is in `failed` state
        :rtype: unicode
        """
        return self._properties['error_code']

    @property
    def error_message(self):
        """
        :returns: Error message describing the failure if the download of the SIM Profile failed and the eSIM Profile is in `failed` state
        :rtype: unicode
        """
        return self._properties['error_message']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the eSIM Profile resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the EsimProfileInstance

        :returns: The fetched EsimProfileInstance
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.EsimProfileInstance {}>'.format(context)
